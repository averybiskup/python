while True:
    print('''
    Enter:
        Display Lines [d]
    ''')

    choice = input('>')

    if choice == 'd':
        n = input('Filename: ')

        f = open(n + '.txt', 'r')

        lines = f.read().split('\n')

        if len(lines) >= 5:
            lines = lines[0:5]
        else:
            pass

        for i in lines:
            print(i)
    else:
        break
