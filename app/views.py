from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # placeholder user object for fake user
    posts = [ # placeholder/fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in PDX!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was slick.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
