from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from models.models import User


class SignupForm(FlaskForm):
    
    username = StringField('username', [Length(min=4, max = 25), DataRequired()])
    email = StringField('email', [Length(min=6, max=50), DataRequired()])
    password = PasswordField('password', [DataRequired()])    
    submit = SubmitField("register")
    
    def valid_username(self, username):
        return User.query.filter_by(username=username).first() is None
       
    def valid_email(self, email):
        return User.query.filter_by(email=email).first() is None

    
    
class LoginForm(FlaskForm):
    pass
    
    
    
