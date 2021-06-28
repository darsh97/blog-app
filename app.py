from flask import Flask

def create_app():
    app = Flask(__name__)
 
    from blueprints.blog import blog

    app.register_blueprint(blog)
    
    return app


