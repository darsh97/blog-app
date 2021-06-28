from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from models import User


class SignupForm(FlaskForm):
    
    username = StringField('username', [Length(min=4, max = 25), DataRequired()])
    email = StringField('email', [Length(min = 6, max = 25), DataRequired()])
    password = PasswordField('password', [DataRequired()])    
    submit = SubmitField("register")
    
    def valid_username(self):
        return User.query.filter_by(username=username.data).first() is None
     
    
    def valid_email(self):
        return User.query.filter_by(email=email.data).first() is None

    
    
    
    
