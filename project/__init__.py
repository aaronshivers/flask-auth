# Import Dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize Database
db = SQLAlchemy()

# Setup the Application
def create_app():

  # Initialize Application
  app = Flask(__name__)
  basedir = os.path.abspath(os.path.dirname(__file__))

  # Configure Application
  app.config['SECRET_KEY'] = 'this-is-a-secret'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Initialize Database
  db.init_app(app)

  # Setup Login Manager
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models import User

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  # Blueprint for Auth Routes
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # Blueprint for Non-Auth Routes
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
