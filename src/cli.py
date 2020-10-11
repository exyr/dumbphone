from typing import Callable

from secrets import PhoneBook
from vimla_api import VimlaAPI

class DumbphoneCLI(object):
    def __init__(self, read: Callable[[], str], write: Callable[[str], None], session: VimlaAPI.Session):
        self.read = read
        self.write = write
        self.session = session
        
    # def startpageData(self, me):
    #     pass
    #
    # def chunks(text):
    #     SMS_MAXIMUM_LENGTH = 120
    #     everything = []
    #     chunk = ''
    #     for line in text.split('\n'):
    #         if len(chunk) + len(line) > SMS_MAXIMUM_LENGTH:
    #             everything.append(chunk[:-1])
    #             chunk = ''
    #         else:
    #             chunk += f'{line}\n'
            
    # def mainMenu(read, write, session: VimlaAPI.Session):
    def mainMenu(self):
        options = [
            'Usage',
            'Saved data',
            'Payments',
            'Referrals',
            'Subscription',
            'Settings',
            'Consent'
        ]

        back = f'Select an option [1-{len(options)}]:'
        # write(back)
        back = ''
        for idx,option in enumerate(options):
            back += f'{idx+1}: {option}\n'
        self.write(back)
        # answer = read()
        # print(f'I got {answer} back')

    def startPage(self):
        me=self.session.readMembersMe()
        print(me)
        name = f"{me['data']['firstName']} {me['data']['lastName']}"
        consumption = me['data']['subscriptions'][0]['consumption']
        voiceCalled = consumption['voice']['spent']
        smsSent = consumption['messages']['spent']
        subscription = consumption['data']['subscription'] / (1000 * 1000 * 1000)
        available = consumption['data']['available'] / (1000 * 1000 * 1000)
        to_send = f'Hello {name}!\nYou have made {voiceCalled} calls and sent {smsSent} messages.\nYou have {round(available,2)}GB left of {round(subscription,0)}GB Monthly'
        self.write(to_send)
        pass

    def settingsPage(read, write, session: VimlaAPI.Session):
        return (
            f''
            f''
            f''
            f''
            f''
            f''
        )

reader = lambda r: print(r)
# writer = lambda _: input()

if __name__ == "__main__":
    token = PhoneBook().get_vimla_token('+46730347518')
    sess = VimlaAPI.Session({"access_token": token})
    print(sess)
    cli = DumbphoneCLI('',reader,sess)
    cli.mainMenu()
    print('----')
    cli.startPage()
    # mainMenu('',reader)
