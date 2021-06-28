from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
bsp = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = "Please log in to access this page"

def create_app():
    app = Flask(__name__)

    bsp.init_app(app)
    db.init_app(app)
    login.init_app(app)

    app.config['SECRET_KEY'] = "ae450ge"
 
    from blueprints.blog import blog
    from blueprints.auth import auth
    
    app.register_blueprint(blog)
    app.register_blueprint(auth, prefix='/auth')
    
    return app


