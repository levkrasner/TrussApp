import  random
import sys
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/test')
def test():
    return 'Testing 123'

@app.route('/test2')
def my_name():
    return 'Lev'

@app.route('/random')
def get_random():
    try:
        n = random.random()
        return str(n)

    except:
        return 'Error'

if __name__ == '__main__':
    app.run()
