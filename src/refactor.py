import urllib
from flask import Flask, request, redirect, render_template
import json
import random
import string

# from cli import mainMenu
from cli import DumbphoneCLI
from secrets import PhoneBook, Secret
from sms_service import send_grpc_sms
from vimla_api import VimlaAPI

app = Flask(__name__)
phonebook = PhoneBook()
secret = Secret()
print(secret)

@app.route('/', methods=['GET'])
def hello_world():
    authorization_url, state = secret.oauth.authorization_url(
        'https://id.wgtwo.com/oauth2/auth',
        nonce=''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
        prompt="login")
    return htmlify(f'''
            <h1>Welcome to Dumbphone</h1>
            <h2>the smart SMS CLI for your subscription</h2>
            <a href="{authorization_url}">Connect</a>
    ''')



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
    phonebook.save_wg2_token(phonenumber, token['access_token'])

    return htmlify(f'''
    <h2>You are now logged via wgtwo on with {phonenumber} </h2>
        <a href=/login/vimla>Connect vimla</a>
    ''')


@app.route('/login/vimla', methods=['GET', 'POST'])
def login_vimla():
    print('got login vimla',request.method,request.method == 'GET')
    if request.method == 'GET':
        return render_template('vimla_login.html')
    # print(repr(request))
    username = request.values['username']
    password = request.values['password']
    session = VimlaAPI.login(username,password)
    number = '+46' + session.readMembersMe()['data']['phoneNumber'][1:]
    phonebook.save_vimla_token(number, session.access_token)
    return htmlify(f'''
    <h2>{username} is all connected</h2> 
    <a href=/sendsms?number={urllib.parse.quote(number)}>sms</a>''')

@app.route('/style.css', methods=['GET'])
def style():
    return render_template('style.css')

@app.route("/sendsms", methods=['GET'])
def send_sms():
    number = request.args.get('number')
    wg2token = phonebook.get_wg2_token(number)
    vimla_token = VimlaAPI.Session({'access_token':phonebook.get_vimla_token(number)})
    cli = DumbphoneCLI('', send_grpc_sms(number, wg2token), vimla_token)
    cli.mainMenu()
    cli.startPage()
    return htmlify(f'<h2>sent menu sms to {number}</h2>')

def htmlify(string):
    return f'''
    <head>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <main>
           {string}
        </main>
    </body>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
