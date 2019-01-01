def up_down(options):
    final = ''
    counter = 0
    choices(options, counter)
    while True:
        ch = input()

        if ch == 'd' or ch == 'down':
            if counter == len(options)-1:
                counter = 0
            else:
                counter += 1

        elif ch == 'u' or ch == 'up':
            if counter == 0:
                counter = len(options)-1
            else:
                counter -= 1

        elif ch == 'y' or ch == 'yes' or ch == '':
            final = options[counter]
            break
        choices(options, counter)
    return final


def choices(options, opt):
    cnt = 0
    for option in options:
        if cnt == opt:
            print('[*]', option)
        else:
            print('[ ]', option)
        cnt += 1