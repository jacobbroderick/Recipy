'''
Recipy is a python based recipe tracker. The idea is that it will sort recipes
based on certain attributes such as time/food required/kitchen utencils etc.


'''

from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
title='Sign in',
form=form)

@app.route("/index")
def main():
    user = {'nickname' : 'Jacob'}
    return render_template('index.html',
title = 'Home',
user = user)
