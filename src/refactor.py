import urllib
from flask import Flask, request, redirect, render_template
import json
import random
import string

from cli import mainMenu
from secrets import PhoneBook, Secret
from sms_service import send_grpc_sms
from vimla_api import VimlaAPI

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
    return f'Welcome to Dumbphone, the smart SMS CLI for your subscription: <a href="{authorization_url}">Login</a>'


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


@app.route('/login/vimla', methods=['GET', 'POST'])
def login_vimla():
    print('got login vimla',request.method,request.method == 'GET')
    if request.method == 'GET':
        return render_template('vimla_login.html')
    # print(repr(request))
    username = request.values['username']
    password = request.values['pwd']
    api = VimlaAPI()
    loginResponse = api.login(username,password)
    print(loginResponse)
    return f'ok gonna login {username}'


@app.route("/sendsms", methods=['GET'])
def send_sms():
    number = request.args.get('number')
    token = phonebook.get_token(number)
    mainMenu('', send_grpc_sms(number, token))
    return f'sent menu sms to {number}'





class DumbphoneCLI(object):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
