from flask import render_template, request, url_for, redirect, flash, jsonify
from urllib.parse import urlsplit
import sqlite3
from app.forms import LoginForm, CreateProfileForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User, Questions, Comments
from sqlalchemy import delete, desc


from app.blueprints import main

@main.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            return redirect("/#login")
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.forum')
        return redirect(next_page)
    return render_template('home.html', title='Home', form=form)

@login_required
@main.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    subtopic = request.form['subtopic']
    title = request.form['title']
    description = request.form['description']

    # Create a new Questions object
    question = Questions(topic=topic, subtopic=subtopic, title=title, description=description, user_id=current_user.id, author=current_user)

    # Add the new object to the session
    db.session.add(question)
    db.session.commit()

    return redirect(url_for('main.thank_you'))

@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@main.route('/profile/<username>')
@login_required
def profile(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts=db.session.scalars(user.questions.select()).all()
    comments=db.session.scalars(user.comments.select()).all()
    return render_template("profile.html", title='Profile', user=user, posts=posts, comments=comments)

@main.route('/forum')
@login_required
def forum():
    all_posts = Questions.query.order_by(desc(Questions.timestamp)).all()
    posts_with_topics = [(post, post.topic, post.subtopic) for post in all_posts]   #List of tuples
    
    grouped_posts = {"All Topics": all_posts}       #Default grouping of all posts 
    for post, topic, subtopic in posts_with_topics:
        if topic not in grouped_posts:
            grouped_posts[topic] = []
        grouped_posts[topic].append(post)       #Goes through the tuples, creates a list of topics 

    topics = list(grouped_posts.keys())     #Grabs the list of topics
    subtopics = {           #Each topic key is mapped to subtopic 
        topic: list(set([subtopic for _, t, subtopic in posts_with_topics if t == topic])) 
        for topic in topics
    }
    return render_template("forum.html", title='Forum', all_posts=all_posts, grouped_posts=grouped_posts, topics=topics, subtopics=subtopics) 

@main.route('/post')
@login_required
def post():
    return render_template("post.html", title='Post')

@main.route('/createProfile', methods=['GET', 'POST'])
def createProfile():
    form = CreateProfileForm()
    if form.validate_on_submit():
        user = User(fname=form.fname.data, lname=form.lname.data, username=form.username.data, email=form.email.data,
                    position=form.position.data, study=form.study.data, bio=form.bio.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template("createProfile.html", title='Create Profile', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Questions.query.get_or_404(post_id)
    comment_text = request.form.get('comment_text')
    if comment_text:
        comment = Comments(comment_text=comment_text, post_id=post_id, user_id=current_user.id, author=current_user)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.viewpost', post_id=post_id))

@main.route('/comments/<int:post_id>')
@login_required
def get_comments(post_id):
    post = Questions.query.get_or_404(post_id)
    comments = [comment.comment_text for comment in post.comments]
    return jsonify(comments)

@main.route('/post/<int:post_id>')
@login_required
def viewpost(post_id):
    post = Questions.query.get_or_404(post_id)
    title = 'ViewPost'  # Assigning the title here
    return render_template("viewpost.html", post=post, title=title)


@main.route('/deleteUser/<int:user_id>')
@login_required
def deleteUser(user_id):
    if (user_id == current_user.id) :
        try: 
            user_to_delete = User.query.get_or_404(user_id)
            logout_user()
            db.session.delete(user_to_delete)

            # delete user's posts and comments
            posts=db.session.scalars(user_to_delete.questions.select()).all()
            for post in posts :
                db.session.delete(post)
            comments=db.session.scalars(user_to_delete.comments.select()).all()
            for comment in comments :
                db.session.delete(comment)

            db.session.commit()
            return redirect(url_for("home"))
        except:
            flash("Account could not be deleted. Try again.", 'error')
            return redirect(url_for("profile", username=current_user.username))

    else :
        redirect(url_for("profile", username=current_user.username))

@main.route('/comment/delete/<int:comment_id>')
@login_required
def delete_comment(comment_id):
    try: 
        comment_to_delete = Comments.query.get_or_404(comment_id)
        if (comment_to_delete.user_id == current_user.id) :
            db.session.delete(comment_to_delete)
            db.session.commit()
            flash("Comment deleted.", 'success')
            return redirect(url_for("profile", username=current_user.username))
        else :
            return redirect(url_for("profile", username=current_user.username))
    except:
        flash("Comment could not be deleted. Try again.", 'error')
        return redirect(url_for("profile", username=current_user.username))
    
@main.route('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    try: 
        post_to_delete = Questions.query.get_or_404(post_id)
        if (post_to_delete.user_id == current_user.id) :
            db.session.delete(post_to_delete)
            db.session.commit()
            flash("Post deleted.", 'success')
            return redirect(url_for("profile", username=current_user.username))
        else :
            return redirect(url_for("profile", username=current_user.username))            
    except:
        flash("Post could not be deleted. Try again.", 'error')
        return redirect(url_for("profile", username=current_user.username))

@main.route('/post/edit/<int:post_id>', methods=['POST'])
@login_required
def editPost(post_id):
    try :
        post_to_edit = Questions.query.get_or_404(post_id)
        if (post_to_edit.user_id == current_user.id) :
            post_to_edit.description = request.form["newPostDescription"]
            db.session.commit()
            flash("Post edited.", 'success')
            return redirect(url_for("profile", username=current_user.username))
        else:
            return redirect(url_for("profile", username=current_user.username)) 
    except :
        flash("Post could not be deleted. Try again.", 'error')
        return  redirect(url_for("profile", username=current_user.username))
    
@main.route('/editProfile', methods=['GET', 'POST'])
@login_required
def editProfile():
    form = EditProfileForm(current_user.username, current_user.email)

    # if request is to submit the editProfile form
    if form.validate_on_submit():
        current_user.fname = form.fname.data
        current_user.lname = form.lname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.position = form.position.data
        current_user.study = form.study.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash("Profile updated.", 'success')
        return redirect(url_for("profile", username=current_user.username))
    
    # if request is to get the editProfile form (with current details filled in)
    elif request.method == 'GET':
        form.fname.data = current_user.fname
        form.lname.data = current_user.lname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.position.data = current_user.position
        form.study.data = current_user.study
        form.bio.data = current_user.bio
    return render_template("editProfile.html", title='Edit Profile', form=form)

@main.route('/post/<int:post_id>')
def viewpost(post_id):
    post = Questions.query.get_or_404(post_id)
    title = 'ViewPost'  # Assigning the title here
    comments = Comments.query.filter_by(post_id=post_id).all()
    return render_template("viewpost.html", post=post, title=title, comments=comments)

@main.route('/search', methods=['POST'])
def search():
    search_term = request.json.get('searchTerm', '')
    if not search_term:
        return jsonify({'error': 'Search term not provided'}), 400
    
    # Query the database for posts and comments that contain the search term
    post_results = Questions.query.filter(
        (Questions.title.ilike(f'%{search_term}%')) |
        (Questions.description.ilike(f'%{search_term}%'))
    ).all()

    # Query the database for comments that contain the search term
    comment_results = Comments.query.filter(Comments.comment_text.ilike(f'%{search_term}%')).all()

    # Serialize the results
    serialized_post_results = [{
        'post_id': result.post_id,
        'title': result.title,
        'description': result.description,
        'username': result.author.username  # Include username
    } for result in post_results]

    serialized_comment_results = [{
        'post_id': result.post_id,
        'comment_id': result.comment_id,
        'comment_text': result.comment_text,
        'username': result.author.username,  # Include username
        'post_title': Questions.query.get(result.post_id).title  # Include the title of the post
    } for result in comment_results]

    return jsonify({'posts': serialized_post_results, 'comments': serialized_comment_results})
