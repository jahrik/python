from flask import render_template, flash, redirect
from app import app
from .forms import PostForm

@app.route('/')
@app.route('/index')
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data)
    return render_template('index.html',
                           title='Home',
                           form=form)
