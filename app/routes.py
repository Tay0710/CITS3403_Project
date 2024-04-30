from flask import render_template, request, url_for, redirect, flash
from urllib.parse import urlsplit
import sqlite3
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from app.forms import CreateProfileForm


@app.route('/', methods=['GET','POST'])
def home():
    #if current_user.is_authenticated:
        #return redirect(url_for('forum'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            return redirect((url_for('home')))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('forum')
        return redirect(next_page)
    return render_template('home.html', title='Home', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    subtopic = request.form['subtopic']
    title = request.form['title']
    description = request.form['description']

    # Store the data in the SQLite database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO questions (topic, subtopic, title, description) VALUES (?, ?, ?, ?)', (topic, subtopic, title, description))
    conn.commit()
    conn.close()

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/profile')
@login_required
def profile():
    validatedUser=True
    user={  'fname' : 'John',
            'lname' : 'Smith',
            'email' : 'student1@uwa.com',
            'position' : 'Undergraduate Student',
            'study' : 'Computer Science',
            'bio' : 'Attending UWA, studying a Bachelor of Science majoring in CompSci and a minor in French. No previous programming experience. Hobbies include hiking and knitting.'
          }
    return render_template("profile.html", user=user, validatedUser=validatedUser, title='Profile')

@app.route('/forum')
@login_required
def forum():
    return render_template("forum.html", title='Forum')

@app.route('/post')
@login_required
def post():
    return render_template("post.html", title='Post')

@app.route('/createProfile', methods=['GET', 'POST'])
def createProfile():
    form = CreateProfileForm()
    if form.validate_on_submit():
        user = User(fname=form.fname.data, lname=form.lname.data, username=form.username.data, email=form.email.data,
                    position=form.position.data, study=form.study.data, bio=form.bio.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("createProfile.html", title='Create Profile', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    