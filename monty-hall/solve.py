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

import random

def openDoor(l, choice):
    print("CHOICE: ", choice)
    print(l, " - FIRST")
    new = list(range(0,3))
    print(new)
    del new[choice]
    print(new)
    del l[random.choice(new)]
    # print(new)


    return l

# Returns an int as an index of the array
def choice():
    return random.randint(0,2)

def createList(i):
    list = [0] * 3
    list[i] = 1

    return list

choice = choice()

l = createList(choice)

print(openDoor(l, choice), " - AFTER")
