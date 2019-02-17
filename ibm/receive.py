from flask import Flask, request, redirect, make_response, current_app
from twilio.twiml.messaging_response import MessagingResponse
import os
from get import *
import json
import functools
from db import *
import random
import emojis

app = Flask('Receiver')

def avg(l):
    return functools.reduce(lambda x, y: x + y, l)

responses_pos = [emojis.encode('Glad to hear you are feeling well!:muscle:'), emojis.encode('Nice, keep up the spirit!:metal:'), emojis.encode('Wow, you sound happy!:smile:')]
responses_neg = [emojis.encode('Perhaps talk to a friend?:raising_hand:'), emojis.encode('What\'s you\'re favorite thing to do? DO IT!:pray:'), emojis.encode('You got this.:muscle:')]


def post_vals(keywords, body, number):
    if len(keywords) > 0:
        sentiment = avg(list(map(lambda x: x['sentiment']['score'], keywords)))
        joy = avg(list(map(lambda x: x['emotion']['joy'], keywords)))
        sadness = avg(list(map(lambda x: x['emotion']['sadness'], keywords)))
        anger = avg(list(map(lambda x: x['emotion']['anger'], keywords)))

        print(sentiment, joy, sadness, anger, body)

        post(number, body, sentiment, joy, sadness, anger)
        return sentiment + joy
    else:
        print('Not enough information')
        return False

@app.route('/sms', methods = ['GET', 'POST'])
def incoming_sms():
    body = str(request.values.get('Body', None))
    number = request.values.get('From', None)
    resp = MessagingResponse()

    if not fetch(number):
        resp.message(emojis.encode('Hello!\nI\'m EMME!:ok_woman: How are you feeling today?'))
        post(number, body)
        return str(resp)

    print(number, body)
    try:
        r = json.loads(process(os.environ['iam_apikey'], body))
    except:
        return ''
    li = r['keywords']

    val = post_vals(li, body, number)
    if val > 0:
        resp.message(random.choice(responses_pos))
        return str(resp)
    elif val <= 0:
        resp.message(random.choice(responses_neg))
        return str(resp)
    else:
        return str(resp)

    return 'Just text me mate.'

@app.route('/db', methods = ['GET', 'POST', 'OPTIONS'])
def get_data():
    num = request.args.get('num')
    key = request.args.get('key')

    if num == None:
        return "The hawk has no number?"
    elif key == None:
        return "Really, no key for the hawk?"
    else:
        try:
            print(num, key)
            d = fetch("+{}".format(num).replace(' ', ''))
            print(d)
            resp = flask.Response("Foo bar baz")
            resp.headers['Access-Control-Allow-Origin'] = '*'
            response = app.response_class(
                response=json.dumps(d),
                status=200,
                mimetype='application/json',
                headers='Access-Control-Allow-Origin'
            )
            return response
        except:
            return "Don't give the hawk bad data, bro."

    print(num, key)
    return "The hawk shall deliver soon."

@app.route('/')
def nothing():
    return "Don't mind me.."

if __name__ == '__main__':
    app.run()
