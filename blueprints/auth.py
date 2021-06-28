from flask import Blueprint, request, url_for, render_template, redirect, flash
from forms.forms import SignupForm
from app import db
from models import User
from flask_login import current_user

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', url_prefix="/auth")



@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    
    form = SignupForm()
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        user = User(username=username, email=email)
        user.set_password_hash(password)
        
        db.session.add(user)
        db.commit()
    
        flash('You are now a registered user!')
        return redirect(url_for('/auth/login'))
        
    return render_template('register.html', form=form, title="Sign up")
    


@auth.route('/login', methods=["GET", "POST"])
def login():
    pass


@auth.route('/logout', methods=["GET"])
def logout():
    pass