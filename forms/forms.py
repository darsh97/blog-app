from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length



class SignupForm(FlaskForm):
    
    username = StringField('username', [Length(min = 4, max = 25),  DataRequired()])
    email = StringField('email', [Length(min = 6, max = 25)])
    password = PasswordField('password', [DataRequired()])    
    
    
    
    
