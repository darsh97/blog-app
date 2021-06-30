from flask import Blueprint, request, url_for, render_template, redirect, flash
from forms.forms import LoginForm, SignupForm
from app import db
from models.models import User
from flask_login import current_user, login_user, logout_user

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
            
            user_name_exists = form.valid_username(username)
            email_exists = form.valid_email(email)
            
            if form.valid_username(username) and form.valid_email(email):
            
                db.session.add(user)
                db.session.commit()
        
                flash('You are now a registered user!')
                return redirect(url_for('auth.login'))
            
            flash("Please try different user name or email", "error")
            
    return render_template('register.html', form=form, title="Sign up")
    


@auth.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if form.user_name_exists(username) and user.check_password(password):
                login_user(user)
                return redirect('/home')
            else:
                flash("Please check username or password", "error")   
                
    return render_template('login.html', title="Login", form=form)



@auth.route('/logout', methods=["GET"])
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('auth.login'))
    