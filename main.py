import firebase_admin
from firebase_admin import firestore, credentials
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

cred = credentials.Certificate("secrets/sgn-test-firestore-access.json")
firebase_admin.initialize_app(cred)

news = firestore.client().collection('news')

@app.route('/')
def hello():
    return 'Welcome to Some Good News API!'

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
