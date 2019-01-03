def up_down(options):
    final = ''
    counter = 0
    length = len(options)
    while True:
        choices(options, counter)

        ch = input('\nSelect option number to go to that option\nPress Enter to Select: ')

        if ch == '':
            final = options[counter%length]
            break

        if ch.isdigit():
            ch = int(ch)
            if ch>length or ch < 1:
                print("\n** Please enter a vaid value **\n")
                continue
            counter = ch - 1

        else:
            print("\n** Please Enter an integer value **\n")
    return final


def choices(options, opt):
    cnt = 0
    for x in range(len(options)):
        option = options[x]
        if cnt == opt:
            print('[' + str(x+1) + '*]', option)
        else:
            print('[' + str(x+1) + ' ]', option)
        cnt += 1