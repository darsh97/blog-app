from flask import Blueprint, render_template
from flask_login import login_required, current_user

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/')
@blog.route('/home')
@login_required
def home():
    if current_user.is_authenticated:
       return render_template('home.html', username=current_user.username)

