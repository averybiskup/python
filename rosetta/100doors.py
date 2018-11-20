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

# For editing each item in list
def iter(l, n, numDoors):
    increment = n

    # This loop is for iterating through loop and changing 1s to 0s and vice versa
    while increment < numDoors:
        l[increment] = 1 if l[increment] == 0 else 0
        increment += n

    return l

# Main function
def getFinalOpenedDoors(numDoors):
    numDoors += 1

    # Create list of 0s
    l = [0] * numDoors
    final = []

    # Applying to each item in list
    for n in range(1, numDoors):
        l = iter(l, n, numDoors)

    # Finding which indexes were 0 at the end
    for i, j in enumerate(l):
        if j == 1:
            final.append(i)

    return final

print(getFinalOpenedDoors(100))
