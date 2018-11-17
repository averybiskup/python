# // There are 100 doors in a row that are all initially closed.
# // You make 100 passes by the doors. The first time through,
# // visit every door and 'toggle' the door (if the door is closed,
# // open it; if it is open, close it). The second time, only visit
# // every 2nd door (i.e., door #2, #4, #6, ...) and toggle it. The
# // third time, visit every 3rd door (i.e., door #3, #6, #9, ...),
# // etc., until you only visit the 100th door.
# //
# //
# // Implement a function to determine the state of the doors
# // after the last pass. Return the final result in an array,
# // with only the door number included in the array if it is open.


def iter(l, n, numDoors):
    increment = n

    while increment < numDoors:
        l[increment] = 1 if l[increment] == 0 else 0
        increment += n

    return l


def getFinalOpenedDoors(numDoors):
    numDoors += 1
    l = [0] * numDoors
    final = []

    for n in range(1, numDoors):
        l = iter(l, n, numDoors)

    for i, j in enumerate(l):
        if j == 1:
            final.append(i)

    return final

print(getFinalOpenedDoors(100))
