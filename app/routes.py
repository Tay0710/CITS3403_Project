from flask import render_template
from app import app
@app.route('/')
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
    return render_template("forum.html", title=title)

@app.route('/post')
def post():
    title='Post'
    return render_template("post.html", title=title)
