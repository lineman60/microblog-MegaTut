__author__ = 'Beryl'
from flask import render_template
from microblog import app

@app.route('/')
@app.route('/index')
def index():
    #passes vars to template
    user = {'nickname': 'Bob'}
    posts = [ #arry of fake posts
        {
            'author': {'nickname': 'Johnny'},
            'body': 'beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'the Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
