while True:
    print('''
    Enter:
        create [c]
        copy to file [cp]
        display content of both [d]
    ''')

    choice = input('>')
    if choice == 'c':
        f_name = input('Filename: ')
        f = open(f_name + '.txt', 'w')
        f.close()
    elif choice == 'cp':
        first_file_name = str(input('File 1: ')) + '.txt'
        second_file_name = str(input('File 2: ')) + '.txt'

        file2 = open(second_file_name, 'w')
        read_file = open(first_file_name, 'r')
        file2.write(read_file.read())

        file2.close()
        read_file.close()
    elif choice == 'd':
        first_file_name = str(input('File 1: ')) + '.txt'
        second_file_name = str(input('File 2: ')) + '.txt'

        r1 = open(first_file_name, 'r')
        r1t = r1.read()
        r2 = open(second_file_name, 'r')
        r2t = r2.read()
        print('File 1:\n\n', r1t)
        print('File 2:\n\n', r2t)
        r1.close()
        r2.close()
    else:
        break
