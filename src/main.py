from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import urllib
import random
import string
import threading

from requests_oauthlib import *

from google import auth as google_auth

from wgtwo.sms.v0 import sms_pb2_grpc, sms_pb2
from wgtwo.common.v0.phonenumber_pb2 import PhoneNumber, TextAddress

import grpc

with open('./secrets.json', mode='r', encoding='utf8') as f:
    secrets = json.load(f)
print(secrets)
PORT = secrets['port']
client_id = secrets['working-group-two']['oauth2']['client_id']
client_secret = secrets['working-group-two']['oauth2']['client_secret']
redirect_uri = secrets['working-group-two']['oauth2']['redirect_uri']

class PhoneBook(object):
    JONATAN = { 'number': '+46738020525', 'token': '<secret>' }
    LUCAS   = { 'number': '+46730347518', 'token': '<secret>' }

def grejsigrunkor():
    VEM = PhoneBook.JONATAN

    call =  grpc.access_token_call_credentials(VEM['token'])
    channel =  grpc.ssl_channel_credentials() 
    combined = grpc.composite_channel_credentials(channel, call)
    channel = grpc.secure_channel('api.wgtwo.com:443', combined)

    stub = sms_pb2_grpc.SmsServiceStub(channel)

    # message =
    x = stub.SendTextToSubscriber(
        sms_pb2.SendTextToSubscriberRequest(
            content='Jag älskar Haskell du hade rätt hela tiden',
            from_text_address=TextAddress(textAddress='Luben'),
            to_subscriber=PhoneNumber(e164=VEM['number'])))
    print(x)
    
scope = 'offline_access openid phone sms.send.to_subscriber'

oauth = OAuth2Session(
    client_id,
    redirect_uri=redirect_uri,
    scope=scope)

authorization_url, state = oauth.authorization_url(
        'https://id.wgtwo.com/oauth2/auth',
        nonce=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        prompt="login")


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()

        if self.path.startswith('/logged-in'):
            print('Oauth callback')
            path = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(path.query)
            print('query')
            print(query)
            self.wfile.write("You want to log on".format(self.path).encode('utf-8'))

            authorization_response = self.path
            token = oauth.fetch_token(
                'https://id.wgtwo.com/oauth2/token',
                authorization_response=authorization_response,
                client_secret=client_secret)
            
            print('token from oauth.fetch_token')
            print(token)        
            r = oauth.get('https://id.wgtwo.com/userinfo')
            print(r.text)
            r.text.phonenumber
        else:
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == "__main__":
    # grejsigrunkor()
    # print("hej")
    threading.Thread(target=oauth).start()
    run()
