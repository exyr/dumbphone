import requests


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
        api_response = requests.request('POST', f'{VimlaAPI.HOST_NAME}/auth/token', data=body).json()
        return VimlaAPI.Session(api_response)


# User Story
#
# Once upon a time, a Vimla user decide to sign up for the Dumphone CLI. Hurrah!
# Good choice, clever Vimla user!
#
#
