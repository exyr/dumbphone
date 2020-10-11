import requests

class Phonebook(object):
    class Contact(object):
        def __init__(self, phonenumber, oauthToken):
            self.phonenumber = phonenumber
            self.oauthToken = oauthToken

class WorkingGroupTwo(object):
    pass

class VimlaAPI(object):
    class Session(object):
        pass

class DumbphoneCLI(object):
    pass

body = {
    "client_id": "P19aGSatiN2D1vfkfzjwTmUu5M9kh1i0",
    "grant_type": "password",
    "password": "p9oVZnm9M1F5",
    "scope": "member member_invoice member.full_control",
    "username": "jonatan.sundqvist@vimla.se"
}

authorizationResponse = requests.request('POST','https://api.vimla.se/auth/token', data=body).json()
print(authorizationResponse)
b = requests.request('GET', 'https://api.vimla.se/members/me/subscriptions/-0/priceplan', headers={ 'Authorization': f'Bearer {authorizationResponse["access_token"]}' })
c = b.json()
print(c)

if __name__ == '__main__':
    pass
