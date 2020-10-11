import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib
import random
import string
import os
from requests_oauthlib import *
from wgtwo.sms.v0 import sms_pb2_grpc, sms_pb2
from wgtwo.common.v0.phonenumber_pb2 import PhoneNumber, TextAddress
import grpc
import codecs

from cli import mainMenu

secretsPath = 'secrets.json'
try:
    secretsPath = os.environ['SECRET_PATH']
    print("using runtime mounted secret")
except:
    print("using default {}".format(secretsPath))

with open(secretsPath, mode='r', encoding='utf8') as f:
    secrets = json.load(f)
PORT = secrets['port']
client_id = secrets['working-group-two']['oauth2']['client_id']
client_secret = secrets['working-group-two']['oauth2']['client_secret']
redirect_uri = secrets['working-group-two']['oauth2']['redirect_uri']

phonebook = {}
try:
    with open('data.json', 'r') as fp:
        phonebook = json.load(fp)
except:
    with open('data.json', 'w') as fp:
        json.dump(phonebook, fp)

def sendSMS(number):
    call = grpc.access_token_call_credentials(phonebook[number])
    channel = grpc.ssl_channel_credentials()
    combined = grpc.composite_channel_credentials(channel, call)
    channel = grpc.secure_channel('api.wgtwo.com:443', combined)

    stub = sms_pb2_grpc.SmsServiceStub(channel)

    def sendWithText(text):
        x = stub.SendTextToSubscriber(
            sms_pb2.SendTextToSubscriberRequest(
                content=text,
                from_text_address=TextAddress(textAddress='Dumbphone C'),
                to_subscriber=PhoneNumber(e164=number)))
        print(x)

    mainMenu('', sendWithText)

def receiveSMS():
    org_id = secrets["working-group-two"]["vimla"]["client_id"]
    org_secret = secrets["working-group-two"]["vimla"]["client_secret"]
    message_bytes = '{}:{}'.format(org_id,org_secret)

    sample_string_bytes = message_bytes.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    basicAuth = "Basic "+base64_bytes.decode("ascii")

    # basicAuth = "Basic {}".format(base64.b64encode('.encode('utf-8')).decode('utf-8'))
    call = grpc.access_token_call_credentials(basicAuth)
    channel = grpc.ssl_channel_credentials()
    combined = grpc.composite_channel_credentials(channel, call)
    channel = grpc.secure_channel('api.wgtwo.com:443', combined)
    stub = sms_pb2_grpc.SmsServiceStub(channel)
    try:
        for sms in stub.ReceiveText(sms_pb2.ReceiveTextRequest()):
            print("got sms",sms)
    except Exception as ex:
        print(repr(ex))


oauth = OAuth2Session(
    client_id,
    redirect_uri=redirect_uri,
    scope='offline_access openid phone sms.send.to_subscriber sms.send.from_subscriber')


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        try:
            path = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(path.query)

            if self.path.startswith('/logged-in'):

                authorization_response = self.path
                params = authorization_response.split('/logged-in')[-1]
                reworked_authorization = redirect_uri + params
                # print("got back:", authorization_response)
                # print("rewriting to:", reworked_authorization)

                token = oauth.fetch_token(
                    'https://id.wgtwo.com/oauth2/token',
                    authorization_response=reworked_authorization,
                    client_secret=client_secret)

                r = oauth.get('https://id.wgtwo.com/userinfo')
                print(r.text)
                phonenumber = json.loads(r.text)['phone_number']
                phonebook[phonenumber] = token['access_token']
                print(phonebook)
                self.wfile.write("You are now logged on with {} <br><a href=/sendsms?number={}>sms</a>".format(phonenumber,phonenumber).encode('utf-8'))
                with open('data.json', 'w') as fp:
                    json.dump(phonebook, fp)

            elif self.path.startswith('/sendsms'):
                number = query['number']
                sendSMS(number)
                self.wfile.write("sent menu to {}".format(number).encode('utf-8'))


            else:
                authorization_url, state = oauth.authorization_url(
                    'https://id.wgtwo.com/oauth2/auth',
                    nonce=''.join(
                        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
                    prompt="login")
                self.wfile.write(
                    "GET request for {}<br><a href='{}'>login</a><br>".format(self.path, authorization_url).encode('utf-8'))
        except Exception as ex:
            print("Error",ex)
            print(repr(ex))
            self.send_error(message="Internal Server Error",code=500)
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = HTTPServer(server_address, S)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == "__main__":
    # receiveSMS()
    run()
