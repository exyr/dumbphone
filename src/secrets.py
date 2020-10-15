import json
import os
from requests_oauthlib import OAuth2Session
from collections import defaultdict

class Secret:
    secretsPath = 'secrets.json'
    try:
        secretsPath = os.environ['SECRET_PATH']
        print("using runtime mounted secret")
    except Exception as ex:
        print("using default {}".format(secretsPath))

    with open(secretsPath, mode='r', encoding='utf8') as f:
        secrets = json.load(f)
    PORT = secrets['port']
    client_id = secrets['working-group-two']['oauth2']['client_id']
    client_secret = secrets['working-group-two']['oauth2']['client_secret']
    redirect_uri = secrets['working-group-two']['oauth2']['redirect_uri']
    oauth = OAuth2Session(
        client_id,
        redirect_uri=redirect_uri,
        scope='offline_access openid phone sms.send.to_subscriber sms.send.from_subscriber')

class PhoneBook:
    phonebook = defaultdict(lambda: {})
    path = 'data.json'

    def __init__(self, path='data.json'):
        self.path = path
        try:
            with open(self.path, 'r') as fp:
                self.phonebook = json.load(fp)
        except:
            self.save()

    def save_wg2_token(self, phonenumber: str, wg2_token: str):
        self.save_phonenumber(phonenumber)
        self.phonebook[phonenumber]['wg2_token'] = wg2_token
        self.save()

    def save_vimla_token(self, phonenumber: str, vimla_token):
        self.save_phonenumber(phonenumber)
        self.phonebook[phonenumber]['vimla_token'] = vimla_token
        self.save()

    def save_phonenumber(self,phonenumber):
        if phonenumber not in self.phonebook:
            self.phonebook[phonenumber] = {}

    def save(self):
        with open(self.path, 'w') as fp:
            json.dump(self.phonebook, fp)


    def get_wg2_token(self, phonenumber: str):
        return self.phonebook[phonenumber]['wg2_token']

    def get_vimla_token(self, phonenumber: str):
        return self.phonebook[phonenumber]['vimla_token']
