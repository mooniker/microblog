from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
