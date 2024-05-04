from flask import render_template, request, url_for, redirect
import sqlite3

from app import app, db
from app.models import Questions

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    subtopic = request.form['subtopic']
    title = request.form['title']
    description = request.form['description']

    # Create a new Questions object
    question = Questions(topic=topic, subtopic=subtopic, title=title, description=description)

    # Add the new object to the session
    db.session.add(question)
    db.session.commit()

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/profile')
def profile():
    title='Profile'
    validatedUser=True
    user={  'fname' : 'John',
            'lname' : 'Smith',
            'email' : 'student1@uwa.com',
            'position' : 'Undergraduate Student',
            'study' : 'Computer Science',
            'bio' : 'Attending UWA, studying a Bachelor of Science majoring in CompSci and a minor in French. No previous programming experience. Hobbies include hiking and knitting.'
          }
    return render_template("profile.html", user=user, validatedUser=validatedUser, title=title)

@app.route('/home')
def home():
    title='Home'
    return render_template("home.html", title=title)

@app.route('/forum')
def forum():
    title='Forum'
    post_list = Questions.query.all()
    grouped_posts = {}
    for post in post_list:
        if post.topic not in grouped_posts:
            grouped_posts[post.topic] = []
        grouped_posts[post.topic].append(post)
    topics = grouped_posts.keys()
    return render_template("forum.html", title=title, grouped_posts=grouped_posts, topics=topics)


@app.route('/post')
def post():
    title='Post'
    return render_template("post.html", title=title)

@app.route('/post/<int:post_id>')
def viewpost(post_id):
    post = Questions.query.get_or_404(post_id)
    return render_template("viewpost.html", post=post)