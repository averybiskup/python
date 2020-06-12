import requests
import json

r = requests.get('https://opentdb.com/api.php?amount=10')

if r.status_code == 200:
    questions = r.json()['results']
    for q in questions:
        question = q['question']
        difficulty = q['difficulty']
        correct = q['correct_answer']
        incorrect = q['incorrect_answers']
        category = q['category']
        #print(q.keys())
        answers = incorrect
        answers.append(correct)
        for answer in answers:
            print(answer)
        print('\n')
