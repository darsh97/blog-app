from flask import Blueprint, request, url_for, render_template
from forms.forms import SignupForm

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        # get all form fields
        # create user object
        # check user name, email validitiy
        # hash password
        # add to db
        # display flash
        # redirect to login
        pass
    
    return render_template('register.html', form=form)
    


@auth.route('/login', methods=["GET", "POST"])
def login():
    pass


@auth.route('/logout', methods=["GET"])
def logout():
    pass