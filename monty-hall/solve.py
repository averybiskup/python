import random

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
swap = False
for i in range(0, times):
    if play(swap):
        correct += 1
print("With Swaps\n" if swap else "Without Swaps\n")
print("Plays:", times)
print("Win percentage: %f" % (correct / times))
