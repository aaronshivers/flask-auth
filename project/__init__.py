# Import Dependencies
from flask import Flask__
from flask_sqlalchemy import SQLAlchemy
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

  # Blueprint for Auth Routes
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # Blueprint for Non-Auth Routes
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app


