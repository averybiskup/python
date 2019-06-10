from flask import Flask, request, render_template

import flask

app = Flask(__name__)

@app.route('/')
def home():
    # return "Hello"
    return render_template('index.html', videoId='q3kSW633bsk')

@app.route('/<videoId>')
def video(videoId):
    return render_template('index.html', videoId=videoId)

if __name__ == "__main__":
    app.run(debug=True)
