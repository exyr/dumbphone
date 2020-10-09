from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import urllib
import random
import string
import threading

from requests_oauthlib import *

# import grpc

# import helloworld_pb2
# import helloworld_pb2_grpc

# # import sms.v0.sms_pb2 as SMSProto
# # import sms.v0.sms_pb2_grpc as grpc
# channel = grpc.insecure_channel('localhost:50051')
# stub = SMSProto.RouteGuideStub(channel)

PORT = 9000

with open('./secrets.json', mode='r', encoding='utf8') as f:
    secrets = json.load(f)
print(secrets)

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
            # '/logged-in?foo=bar'
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

def oauth():
    client_id = secrets['working-group-two']['oauth2']['client_id']
    client_secret = secrets['working-group-two']['oauth2']['client_secret']
    redirect_uri = 'https://jonatan-raw.vimla.work/logged-in'

    scope = 'offline_access openid phone sms.send.to_subscriber'
    oauth = OAuth2Session(
        client_id,
        redirect_uri=redirect_uri,
        scope=scope)
    
    authorization_url, state = oauth.authorization_url(
            'https://id.wgtwo.com/oauth2/auth',
            nonce=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
            prompt="login")

    print(state)
    print('Please go to %s and authorize access.' % authorization_url)
    authorization_response = input('Enter the full callback URL')

    token = oauth.fetch_token(
        'https://id.wgtwo.com/oauth2/token',
        authorization_response=authorization_response,
        client_secret=client_secret)
    
    print()
    print(token)

    r = oauth.get('https://id.wgtwo.com/userinfo')
    print('RRRRRgggg')
    print(r.text)
    # Enjoy =)

if __name__ == "__main__":
    print("hej")
    threading.Thread(target=oauth).start()
    run()
