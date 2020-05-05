"""
    Function that takes a list from the user, and prints the list, and the list with the largest element replaced with the first element.
"""
def swap():

    list = []
    
    while True:
        num = input('')

        if num == 'q':
            break

        list.append(int(num))

    print(list)
    largest = max(list)
    largest_index = list.index(largest)
    first = list[0]
    list[0] = largest
    list[largest_index] = first
    print(list)

swap()
