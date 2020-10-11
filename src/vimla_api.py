import requests


class VimlaAPI(object):
    HOST_NAME = 'https://api.vimla.se'
    CLIENT_ID = 'P19aGSatiN2D1vfkfzjwTmUu5M9kh1i0'

    class Session(object):
        def __init__(self, authorization):
            self.__dict__.update(authorization)
            self.headers = {'Authorization': f'Bearer {self.access_token}'}

        def readPriceplan(self):
            return requests.request('GET', f'{VimlaAPI.HOST_NAME}/members/me/subscriptions/-0/priceplan', headers=self.headers).json()
        
        def readMembersMe(self):
            return requests.request('GET', f'{VimlaAPI.HOST_NAME}/members/me/', headers=self.headers).json()

    @staticmethod
    def login(username: str, password: str):
        body = {
            'client_id': VimlaAPI.CLIENT_ID,
            'grant_type': 'password',
            'scope': 'member member_invoice member.full_control',
            'username': username,
            'password': password
        }
        response = requests.request('POST', f'{VimlaAPI.HOST_NAME}/auth/token', data=body)
        if response.status_code == 200:
            return VimlaAPI.Session(response.json())
        else:
            print(f'Failed to log on with username {username}')

# User Story
#
# Once upon a time, a Vimla user decide to sign up for the Dumphone CLI. Hurrah!
# Good choice, clever Vimla user!
#
#
