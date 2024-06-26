from flask import render_template
from app import db
from app.blueprints import main

@main.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Directly from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling