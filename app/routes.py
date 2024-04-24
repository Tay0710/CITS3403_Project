from flask import render_template, request, url_for, redirect, flash
import sqlite3

from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/forum')
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
def forum():
    return render_template("forum.html", title='Forum')

@app.route('/post')
def post():
    return render_template("post.html", title='Post')
    