'''
    Function that takes a list from user, and outputs largest and smallest elements.
'''
def getUniques():
    
    list = []

    while True:
        num = input('')

        if num == 'q':
            break

        list.append(int(num))

    print('Largest: {} | Smallest: {}'.format(max(list), min(list)))

getUniques()
