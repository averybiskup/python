import random

with open('./list.txt', 'r') as file:
    data = file.read()

activities = data.split('\n')

def getRandom():
    return random.choice(activities)

print(getRandom())
