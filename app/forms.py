from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField, TextAreaField, EmailField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class CreateProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Length(min=1, max=64)])
    lname = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=64)])
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=1, max=120)])
    position = RadioField('Position', choices=[
        ('Undergraduate Student', 'Undergraduate Student'),
        ('Postgraduate Student', 'Postgraduate Student'),
        ('Staff', 'Staff'),
        ('Future Student', 'Future Student'),
        ('Graduate', 'Graduate')
    ], validators=[DataRequired()])
    study = SelectField('Area of Study', choices=[
        ('Accounting', 'Accounting'),
        ('Agricultural Science', 'Agricultural Science'),
        ('Anatomy and Human Biology', 'Anatomy and Human Biology'),
        ('Anthropology', 'Anthropology'),
        ('Architecture', 'Architecture'),
        ('Asian Studies', 'Asian Studies'),
        ('Biochemistry', 'Biochemistry'),
        ('Botany', 'Botany'),
        ('Business Law', 'Business Law'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Chemistry', 'Chemistry'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Classical Studies', 'Classical Studies'),
        ('Computer Science', 'Computer Science'),
        ('Conservation Biology', 'Conservation Biology'),
        ('Data Science', 'Data Science'),
        ('Dentistry', 'Dentistry'),
        ('Earth Sciences', 'Earth Sciences'),
        ('Economics', 'Economics'),
        ('Education', 'Education'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Environmental Engineering', 'Environmental Engineering'),
        ('Environmental Science', 'Environmental Science'),
        ('Finance', 'Finance'),
        ('French Studies', 'French Studies'),
        ('Genetics', 'Genetics'),
        ('Geography', 'Geography'),
        ('Geology', 'Geology'),
        ('History', 'History'),
        ('Human Resource Management', 'Human Resource Management'),
        ('Indigenous Knowledge, History, and Heritage', 'Indigenous Knowledge, History, and Heritage'),
        ('Indonesian Studies', 'Indonesian Studies'),
        ('Information Technology', 'Information Technology'),
        ('Japanese Studies', 'Japanese Studies'),
        ('Law', 'Law'),
        ('Linguistics', 'Linguistics'),
        ('Management', 'Management'),
        ('Marine Science', 'Marine Science'),
        ('Marketing', 'Marketing'),
        ('Mathematics', 'Mathematics'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Medicine', 'Medicine'),
        ('Microbiology', 'Microbiology'),
        ('Music', 'Music'),
        ('Neuroscience', 'Neuroscience'),
        ('Nursing', 'Nursing'),
        ('Petroleum Engineering', 'Petroleum Engineering'),
        ('Philosophy', 'Philosophy'),
        ('Physics', 'Physics'),
        ('Physiology', 'Physiology'),
        ('Political Science and International Relations', 'Political Science and International Relations'),
        ('Psychology', 'Psychology'),
        ('Public Health', 'Public Health'),
        ('Renewable Energy Engineering', 'Renewable Energy Engineering'),
        ('Social Work', 'Social Work'),
        ('Sociology', 'Sociology'),
        ('Spanish Studies', 'Spanish Studies'),
        ('Sport Science', 'Sport Science'),
        ('Statistics', 'Statistics'),
        ('Sustainable Development', 'Sustainable Development'),
        ('Theatre Studies', 'Theatre Studies'),
        ('Urban and Regional Planning', 'Urban and Regional Planning'),
        ('Zoology', 'Zoology')
    ], validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired(),  Length(min=1, max=200)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Profile')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('This username is already taken.')    
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('This email is already used.')    