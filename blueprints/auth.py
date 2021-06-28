from flask import Blueprint, request, url_for, render_template, redirect, flash
from forms.forms import LoginForm, SignupForm
from app import db
from models.models import User
from flask_login import current_user

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', url_prefix="/auth")

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            user = User(username=username, email=email)
            user.set_password_hash(password)
            
            if form.valid_username(username) and form.valid_email(email):
            
                db.session.add(user)
                db.session.commit()
        
                flash('You are now a registered user!')
                return redirect(url_for('auth.login'))
            
            
    return render_template('register.html', form=form, title="Sign up")
    


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login")


@auth.route('/logout', methods=["GET"])
def logout():
    pass