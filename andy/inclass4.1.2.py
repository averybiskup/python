while True:
    print('''
    Enter:
        create [c]
        display # of lines [l]
        display content [d]
    ''')

    choice = input('>')
    if choice == 'c':
        f_name = input('Filename: ')
        f = open(f_name + '.txt', 'w')
        f.close()
        break
    elif choice == 'l':
        f_name = input('Filename: ')
        f = open(f_name, 'r')
        lines = len(f.read().split('\n')) - 1
        print(lines)
        break
    elif choice == 'd':
        f_name = input('Filename: ')
        f = open(f_name, 'r')
        print(f.read())
        break
    else:
        break
