from vimla_api import VimlaAPI

class DumbphoneCLI(object):
    def __init__(self, read: Callable[[], str], write: Callable[[str], Void], session: VimlaAPI.Session):
        self.read = read
        self.write = write
        self.session = session
        
    def startpageData(self, me):
        pass

    def chunks(text):
        SMS_MAXIMUM_LENGTH = 120
        everything = []
        chunk = ''
        for line in text.split('\n'):
            if len(chunk) + len(line) > SMS_MAXIMUM_LENGTH:
                everything.append(chunk[:-1])
                chunk = ''
            else:
                chunk += f'{line}\n'
            
    def mainMenu(read, write, session: VimlaAPI.Session):
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
        write(back)
        # answer = read()
        # print(f'I got {answer} back')

    def startPage(read, write, session: VimlaAPI.Session):
        me=session.readMembersMe()
        name = f"{me['data']['firstName']} {me['data']['lastName']}"
        consumption = me['data']['subscriptions'][0]['consumption']
        voiceCalled = consumption['voice']['spent']
        smsSent = consumption['messages']['spent']
        subscription = consumption['data']['subscription']
        available = consumption['data']['available']
        to_send = f'Hello {name}!\nYou have made {voiceCalled} calls and sent {smsSent} messages.\nYou have {available}GB left of {perMonth}GB Monthly'
        write(to_send)
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
    mainMenu('',reader)
