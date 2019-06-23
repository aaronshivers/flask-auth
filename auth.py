# Import Dependencies
from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

@main.route('/login')
def login():
  return 'Login'

@main.route('/signup')
def signup():
  return 'Signup'

@main.route('/logout')
def logout():
  return 'Logout'