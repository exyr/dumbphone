import requests
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Your phone is DUMB AS FUCK'

@app.route('/logged-in', methods=['GET'])
def logged_in():
    authorization_response = request.url
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

class Phonebook(object):
    class Contact(object):
        def __init__(self, phonenumber, oauthToken):
            self.phonenumber = phonenumber
            self.oauthToken = oauthToken

class WorkingGroupTwo(object):
    pass

class VimlaAPI(object):
    HOST_NAME = 'https://api.vimla.se'
    CLIENT_ID = 'P19aGSatiN2D1vfkfzjwTmUu5M9kh1i0'

    class Session(object):
        def __init__(self, authorization):
            self.__dict__.update(authorization)
            self.headers = { 'Authorization': f'Bearer {self.access_token}' }

        def readPriceplan(self):
            return requests.request('GET', f'{VimlaAPI.HOST_NAME}/members/me/subscriptions/-0/priceplan', headers=self.headers).json()
    
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
