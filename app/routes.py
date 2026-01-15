from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Denys'}
    posts = [
        {
            'author': {'username': 'Denys', "body": "What the fuck", "likes": 25}
        },
        {
            'author': {'username': 'Lilia', 'body': "Holy shit", "likes": 9090}
        }
    ]

    return render_template('index.html', title="Home", user=user, posts=posts)
