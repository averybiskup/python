def create_golfer():
    f = open('golf.txt', 'a+')

    name = input('Name: ')
    score = input('Score: ')

    f.write('Name: {} | Score: {}\n'.format(name, score))

def read():
    f = open('golf.txt', 'r')
    print('---Records---')
    print(f.read())
    print('-------------')

def search():
    name = input('Name: ')

    f = open('golf.txt', 'r')
    lines = f.read().split('\n')
    for i in lines:
        if name.lower() in i.lower():
            print('\nRecord Found: ')
            print(i)
            print('-------------')
            return True
    print('Record not found.')
    print('-------------')


while True:
    print('''
    Enter:
        Create Golfer [c]
        Display Records [r]
        Search Golfers [s]
    ''')

    choice = input('>')

    if choice == 'c':
        create_golfer()
    elif choice == 'r':
        read()
    elif choice == 's':
        search()
    else:
        break
