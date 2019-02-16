from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
from get import *
import json

# r = process(os.environ['iam_apikey'])

app = Flask('Receiver')

@app.route('/sms', methods = ['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    r = json.loads(process(os.environ['iam_apikey'], body))
    li = r['keywords']
    # mood = 0






    return 'Just text me mate.'

@app.route('/')
def nothing():
    return "Don't mind me.."

if __name__ == '__main__':
    app.run()
