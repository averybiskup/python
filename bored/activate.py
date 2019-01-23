import random

activities = [
              'Leet Code',
              'Wash Dishes',
              'Read for 25 minutes',
              'Take a walk',
              'Pull ups',
              'Audio Book',
              'Read Medium',
              'Ride Bike',
              'Homework',
              'Push ups',
              'Duo Lingo',
              'Elevate',
             ]

def getRandom():
    return random.choice(activities)

print(getRandom())
