import urllib
from flask import request
import requests
from flask import Flask, request, redirect
from requests_oauthlib import *
import json
import random
import string

from cli import mainMenu
from secrets import PhoneBook, Secret
from sms_service import send_grpc_sms

app = Flask(__name__)
phonebook = PhoneBook()
secret = Secret()


@app.route('/', methods=['GET'])
def hello_world():
    authorization_url, state = secret.oauth.authorization_url(
        'https://id.wgtwo.com/oauth2/auth',
        nonce=''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        prompt="login")
    return f'Your phone is DUMB AS FUCK <a href="{authorization_url}">login</a>'


@app.route('/logged-in', methods=['GET'])
def logged_in():
    authorization_response = request.url
    params = authorization_response.split('/logged-in')[-1]
    reworked_authorization = secret.redirect_uri + params

    token = secret.oauth.fetch_token(
        'https://id.wgtwo.com/oauth2/token',
        authorization_response=reworked_authorization,
        client_secret=secret.client_secret)

    r = secret.oauth.get('https://id.wgtwo.com/userinfo')
    phonenumber = json.loads(r.text)['phone_number']
    phonebook.save(phonenumber, token['access_token'])
    return f'You are now logged on with {phonenumber} <br><a href=/sendsms?number={urllib.parse.quote(phonenumber)}>sms</a> '

@app.route("/sendsms", methods=['GET'])
def send_sms():
    number = request.args.get('number')
    token = phonebook.get_token(number)
    mainMenu('', send_grpc_sms(number, token))
    return f'sent menu sms to {number}'



class VimlaAPI(object):
    HOST_NAME = 'https://api.vimla.se'
    CLIENT_ID = 'P19aGSatiN2D1vfkfzjwTmUu5M9kh1i0'

    class Session(object):
        def __init__(self, authorization):
            self.__dict__.update(authorization)
            self.headers = {'Authorization': f'Bearer {self.access_token}'}

        def readPriceplan(self):
            return requests.request('GET', f'{VimlaAPI.HOST_NAME}/members/me/subscriptions/-0/priceplan',
                                    headers=self.headers).json()

    @staticmethod
    def login(username, password):
        body = {
            'client_id': VimlaAPI.CLIENT_ID,
            'grant_type': 'password',
            'scope': 'member member_invoice member.full_control',
            'username': username,
            'password': password
        }

        return VimlaAPI.Session(requests.request('POST', f'{VimlaAPI.HOST_NAME}/auth/token', data=body).json())


# User Story
# 
# Once upon a time, a Vimla user decide to sign up for the Dumphone CLI. Hurrah!
# Good choice, clever Vimla user!
#
# 


class DumbphoneCLI(object):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
