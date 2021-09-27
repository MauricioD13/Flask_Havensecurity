import os
import random

from werkzeug.security import generate_password_hash

class Config_development:
    SECRET_KEY = 'super_secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mauro:mauro9812@localhost/flaskmysql'

    ENV = 'development'

class Config_production:

    SLQALCHEMY_DATABASE_URI = 'mysql+pymysql://b035ea528c9790:a75c1722@us-cdbr-east-04.cleardb.com/heroku_273f36d63cbccb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'production'
    DEBUG = False

    SECRET_KEY = generate_password_hash(str(random.randint(100, 200)))