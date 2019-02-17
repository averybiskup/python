import firebase_admin
from firebase_admin import credentials, firestore
import time

#Built with: Python, Flask, FireBase, Twilio, IBM Natural Language Understanding,

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tracker-668bb.firebaseio.com/'
})

db = firestore.client()

def post(num, text, sentiment=0, joy=0, sadness=0, anger=0):
    date = str(time.strftime("%S-%M-%H-%d-%m-%y"))
    doc_ref = db.collection('EMME').document('users').collection(num).document(date)
    doc_ref.set({
                    'text': text,
                    'sentiment': sentiment,
                    'joy': joy,
                    'sadness': sadness,
                    'anger': anger
        })
    print("Posted.")

def fetch(num):
    try:
        r = db.collection('EMME').document('users').collection(num).get()

        res = []
        for i in r:
            res.append(i.to_dict())

        if len(res) <= 0:
            print('Document empty')
            return False
        return res
    except:
        print('No such document')
        return 'No such ducument'
