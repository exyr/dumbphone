def mainMenu(read,write):
    options = [
        'Usage',
        'Saved data',
        'Payments',
        'Referrals',
        'Subscription',
        'Settings',
        'Consent'
    ]

    back = 'select a number:\n'
    for idx,option in enumerate(options):
        back += f'{idx}: {option}\n'
    write(back)
    # answer = read()
    # print(f'I got {answer} back')

reader = lambda r: print(r)
# writer = lambda _: input()

if __name__ == "__main__":
    mainMenu('',reader)
