import requests
import json
import sys
import os
import time
from figlet_wrapper import p

r = requests.get('https://opentdb.com/api.php?amount=10')

os.system('clear')
print(p('Welcome to Trivia!', 'slant', 'cyan'))
time.sleep(2)

if r.status_code != 200:
    print('Something went wrong')
    sys.exit()

current = 0
questions = r.json()['results']


def list_to_obj(l):
    obj = {}

    for i, l in enumerate(l):
        obj[i + 1] = l

    return obj

while current < len(questions):
    os.system('clear')
    q = questions[current]
    question = q['question']
    difficulty = q['difficulty']
    correct = q['correct_answer']
    incorrect = q['incorrect_answers']
    category = q['category']
    answers = incorrect
    answers.append(correct)
    
    a_obj = list_to_obj(answers)
    

    print(question + '\n')

    for n, a in a_obj.items():
        print('[' + str(n) + ']', a)

    user_a = input('>')

    os.system('clear')
    if user_a == 'q':
        print(p('Bai', 'r', 'cyan'))
        break
    elif a_obj[int(user_a)] == correct:
        print(p('nice', 'r', 'green'))
    else:
        print(p('not nice', 'r', 'red'))
        print(correct)

    time.sleep(1)

    current += 2

print('Game Over')



list_to_obj(['hi', 'no'])


