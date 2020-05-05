"""
    This function gets the unique values of the numbers inputted from users.
    It also prints the max, and min of the numbers.
"""

def getUniques():
    print('Please enter some positive integers, hitting return after each on. Enter \'q\' to quit:\n')

    list = []
    while True:
        num = input('')

        if num == 'q':
            break

        if not num.isdecimal():
            break

        if int(num) not in list and int(num) >= 0:
            list.append(int(num))

    print('You entered {} unique numbers:\n'.format(len(list)))
    for i in list:
        print(i, end=' ')

    print('\nWith minimum value: {} and maximum value: {}'.format(min(list), max(list)))


def main():
    getUniques()

if __name__ == '__main__':
    main()
