__author__ = 'Beryl'
from flask import render_template, flash, redirect
from __init__ import app
from forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remeber_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
