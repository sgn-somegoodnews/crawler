from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Some Good News API!'

@app.route('/update-news')
def updateNews():
    return "Update news route called. Yet to be implemented"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
