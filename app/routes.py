from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    render_template("profilePage.html")