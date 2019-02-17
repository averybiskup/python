from pylab import *
import numpy as np

from db import *

def create(e):
    t = arange(0, int(len(e['sadness'])))
    sad = np.array(e['sadness'])
    joy = np.array(e['joy'])
    anger = np.array(e['anger'])
    sentiment = np.array(e['sentiment'])

    w = 4
    plot(t, sad, color='orange', linewidth=w)
    plot(t, joy, color='green', linewidth=w)
    plot(t, anger, color='red', linewidth=w)
    plot(t, sentiment, color='blue', linewidth=w)

    l1, = plt.plot([0,0], label='Sentiment')
    l2, = plt.plot([0,0], label='Sadness')
    l3, = plt.plot([0,0], label='Joy')
    l4, = plt.plot([0,0], label='Anger')
    plt.legend([l1, l2, l3, l4], ['Sentiment', 'Sadness', 'Joy', 'Anger'])

    title('Weekly Analysis')
    grid(True)
    show()

def graph(num):
    d = fetch(num)
    emotions = {
        'sadness': [],
        'sentiment': [],
        'joy': [],
        'anger': []
    }

    for i in list(d):
        emotions['sadness'].append(i['sadness'])
        emotions['sentiment'].append(i['sentiment'])
        emotions['joy'].append(i['joy'])
        emotions['anger'].append(i['anger'])

    create(emotions)

graph(sys.argv[1])
