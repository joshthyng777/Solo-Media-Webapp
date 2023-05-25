from flask import Flask, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfajihlmnxujs 12387 solo media'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Weight

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

# trying to define the api route for axios on the front end but am not sure how just yet
# Was thinking of creating a different file for it called routes.py but figured i'd hold off on that for now
# @app.route('/api/data', methods=['GET'])
# def get_data():
    # Handle the GET request and return the response
    # data = {
     #   'message': 'Hello from the backend!',
     #   'data': [1, 2, 3, 4, 5]
   # }
    #return jsonify(data)

if __name__ == '__main__':
    app.run()
