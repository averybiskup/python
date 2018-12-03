# The Monty Hall problem is from a game show where there
# are three doors: 2 with goats (or something bad), and 1
# with a car.
# First: the player chooses one door
# Second: the player is shown one of the doors with a goat in it
# Third: the player is asked weather he/she wants to switch their choice
# Fourth: whichever door the player ends with, he/she gets that prize
#
# The problem:
# Is it best to switch your choice or keep with your door.
#
# Solution:
# If you don't switch, you have 33% of getting the car
#
# If you do switch you have 66% of getting the car,
# because you have seen 2 doors
#
# ALWAYS SWITCH

#This program tests this theory with a brute force method

# Steps to program:
# Inhabit list of two 0s and a 1
# pick random element
# run many times
# log results


def openDoor(l, choice):
    for i, j in enumerate(l):
        if j == 0 and i != choice:
            del l[i]
    return l


def choice():
    return random.randint(0,2)

def createList():
    list = [0] * 3
    list[random.randint(0,2)] = 1

    return list

l = createList()

print(openDoor(l, choice()))

# l = [0, 1, 0]

# first = random.choice(l)
