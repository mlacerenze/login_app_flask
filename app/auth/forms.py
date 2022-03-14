from tokenize import String 
from flask import Flask 
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, PasswordField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# email_exists
def email_exists(form, field):
  email = User.query.filter_by(user_email=field.data).first()
  if email:
    raise ValidationError('Email already exists.')

class RegistrationForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired(), Length(4,16, message='Between 4 to 16 chars.')]) # (4, 16) min - max characteres
  email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Password must match')])
  confirm = PasswordField('Confirm', validators=[DataRequired()])
  submit = SubmitField('Register')
  
class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  stay_loggedin = BooleanField('Remember Me')
  submit = SubmitField('Login')
  
# form to scrapy
class ScrapyForm(FlaskForm):
  search_article = StringField('Search Article', validators=[DataRequired()])
  submit = SubmitField('Search')