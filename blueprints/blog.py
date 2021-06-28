from flask import Blueprint

blog = Blueprint('blog', __name__)

@blog.route('/')
def home():
    return "<h1> Blog home page"
    