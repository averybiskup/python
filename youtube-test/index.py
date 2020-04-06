from flask import *
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', videoId='YFeqYRuRwtY')

@app.route('/<videoId>')
def video(videoId):
    return render_template('index.html', videoId=videoId)

if __name__ == "__main__":
    app.run(debug=True)
