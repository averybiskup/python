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

# NOT PUSHED YET
def play(withSwap):

    # Gets indexes for car and guess
    car = random.randint(0, 2)
    guess = random.randint(0, 2)

    # For solving which door isn't car nor guess
    temp = [0] * 3
    temp[guess] = 1
    temp[car] = 1
    goat = temp.index(0)

    if withSwap:

        # Chooses to either swap, or stay with the same guess
        test = [guess, car]
        guess = random.choice(test)

    return guess == car


# Play some amount of times
correct = 0
times = 100000
swap = True
for i in range(0, times):
    if play(swap):
        correct += 1
print("With Swaps\n" if swap else "Without Swaps\n")
print("Plays:", times)
print("Win percentage: %f" % (correct / times))
