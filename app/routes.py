from flask import render_template, request, url_for, redirect, jsonify
import sqlite3

from app import app, db
from app.models import Questions, Comments

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
    print(post_list)
    return render_template("forum.html", title=title, post_list=post_list)

@app.route('/post')
def post():
    title='Post'
    return render_template("post.html", title=title)

@app.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    post = Questions.query.get_or_404(post_id)
    comment_text = request.form.get('comment_text')
    if comment_text:
        comment = Comments(comment_text=comment_text, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('viewpost', post_id=post_id))

@app.route('/comments/<int:post_id>')
def get_comments(post_id):
    post = Questions.query.get_or_404(post_id)
    comments = [comment.comment_text for comment in post.comments]
    return jsonify(comments)

@app.route('/post/<int:post_id>')
def viewpost(post_id):
    post = Questions.query.get_or_404(post_id)
    title = 'ViewPost'  # Assigning the title here
    return render_template("viewpost.html", post=post, title=title)
