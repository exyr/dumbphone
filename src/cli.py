def mainMenu(read,write):
    options = ['Usage','Saved data','Payments','Referrals','Subscription','Settings','Consent']
    back = 'select a number:\n'
    for idx,option in enumerate(options):
        back += "{0}: {1}\n".format(idx,option)
    write(back)
    # awnser = read()
    # print('i got '+awnser+" back")

reader = lambda r: print(r)
# writer = lambda _: input()

if __name__ == "__main__":
    mainMenu('',reader)
