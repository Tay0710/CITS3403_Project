from flask import render_template
from app import app
@app.route('/')
@app.route('/profile')
def profile():
    validatedUser=True
    user={  'fname' : 'John',
            'lname' : 'Smith',
            'email' : 'student1@uwa.com',
            'position' : 'Undergraduate Student',
            'study' : ['Computer Science', 'French'],
            'bio' : 'Attending UWA, studying a Bachelor of Science majoring in CompSci and a minor in French. No previous programming experience. Hobbies include hiking and knitting.'
          }
    return render_template("profilePage.html", user=user, validatedUser=validatedUser)

@app.route('/createProfile')
def createProfile():
    return render_template("createProfile.html")