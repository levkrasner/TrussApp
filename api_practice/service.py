from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/gethi')
def say_hi():
    return 'Hi'

if __name__ == '__main__':
    app.run()
