from distutils.log import Log 
from ensurepip import bootstrap
import os
import bcrypt
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap 
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt 

db = SQLAlchemy() # create database
bootstrap = Bootstrap() # import styles
bcrypt = Bcrypt() # create instance to encript passwords
login_manager = LoginManager()
login_manager.login_view = 'authentication.log_in_user'
login_manager.session_protection = 'strong'

def create_app(config_type):
  app = Flask(__name__)
  configuration = os.path.join(os.getcwd(), 'config', config_type + '.py') # browse a file and convert to .py file
  app.config.from_pyfile(configuration)
  
  # init all
  db.init_app(app)
  bootstrap.init_app(app)
  login_manager.init_app(app)
  bcrypt.init_app(app)
  
  from app.auth import authentication
  app.register_blueprint(authentication)
  
  return app 