from flask import Blueprint

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/')
def index():
    return "<h1> welcome </h1>"