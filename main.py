import firebase_admin
from firebase_admin import firestore, credentials
from flask import Flask, jsonify, request
import datetime

from tweet import find_tweets

app = Flask(__name__)

cred = credentials.Certificate("secrets/sgn-test-firestore-access.json")
firebase_admin.initialize_app(cred)

news = firestore.client().collection('news')

def coerce(num, min, max):
    if (num < min):
        return min
    if (num > max):
        return max
    return num

@app.route('/')
def hello():
    return 'Welcome to Some Good News API!'

@app.route('/tweets')
def tweets():
    query = request.args.get('query')
    if (query == None or len(query.strip()) < 1):
        return 'Please provide a valid query.', 422

    num = coerce(int(request.args.get('num') or '10'), 0, 10)

    results = find_tweets(query, num)
    return jsonify(results)

@app.route('/update-news')
def updateNews():
    print("Update news route called, creating random news.")

    new = {
        'headline': 'Breaking News! BE provided new',
        'subheadline': 'This new was completely created by BE',
        'image': 'https://images.unsplash.com/photo-1570700258112-e259d3dbafb4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80',
        'timestamp': datetime.datetime.now(),
        'url': 'https://some-good-news.uc.r.appspot.com/'
    }

    news.document().set(new)
    return jsonify(new), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
