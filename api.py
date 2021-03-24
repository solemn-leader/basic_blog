import flask
from flask import request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# 127.0.0.1/home
@app.route('/home', methods=['GET'])
def home():
    return '<h1>Home</h1>'

app.run(
    host='127.0.0.1'
)
