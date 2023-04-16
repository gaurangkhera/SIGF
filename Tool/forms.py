from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField, IntegerField, RadioField, DateField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError
from Tool import app, db
from flask_login import current_user
from Tool.models import User


class RegistrationForm(FlaskForm):
    phone1 = IntegerField('phone1', validators=[DataRequired()])
    phoneb = IntegerField('phoneb', validators=[DataRequired()])
    email1 = StringField('Email1', validators=[DataRequired(), Email()])
    emailb = StringField('Emailb', validators=[DataRequired(), Email()])
    name1 = StringField('name1', validators=[DataRequired()])
    name2 = StringField('name2', validators=[DataRequired()])
    name3 = StringField('name3', validators=[DataRequired()])
    name4 = StringField('name4')
    school1 = StringField('school1', validators=[DataRequired()])
    school2 = StringField('school2', validators=[DataRequired()])
    school3 = StringField('school3', validators=[DataRequired()])
    school4 = StringField('school4')
    am_name = StringField('adult mentor name', validators=[DataRequired()])
    am_email = StringField('adult mentor email', validators=[DataRequired()])
    am_phone = StringField('adult phone', validators=[DataRequired()])
    submit = SubmitField('Register')
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match.'), Length(min=8, max=16)])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(
                'Email taken.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(
                'Username taken.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    radio = RadioField('Select', choices=[
                       'Recruitment', 'Outreach', 'Graphics Design', 'Social Media Management'])
    submit = SubmitField('Submit application')
    
class SIGFform(FlaskForm):
    f_name = StringField('name', validators=[DataRequired()])
    school = StringField('school', validators=[DataRequired()])
    email = StringField('name', validators=[DataRequired()])
    age = IntegerField('name', validators=[DataRequired()])
    writeup = TextAreaField('writeup', validators=[DataRequired()])
    city = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
