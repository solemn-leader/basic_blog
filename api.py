import flask
from flask import request
import os

port = int(os.environ.get('PORT', 5000))

app = flask.Flask(__name__)
app.config['DEBUG'] = True

posts = []

@app.route('/feed', methods=['GET'])
def feed():
    return '<br>'.join(posts)

@app.route('/add_post', methods=['GET'])
def add_post():
    post = str(request.query_string).replace('%20', ' ')[2: -1]
    posts.append(post)
    return post

app.run(
    host='0.0.0.0',
    port=port
)
