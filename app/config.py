import random
from datetime import timedelta
from werkzeug.security import generate_password_hash

class Config_development:
    SECRET_KEY = 'super_secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mauro:mauro9812@localhost/flaskmysql'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'


class Config_production:
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'production'
    DEBUG = False
    REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b035ea528c9790:a75c1722@us-cdbr-east-04.cleardb.com/heroku_273f36d63cbccb4'
    SECRET_KEY = generate_password_hash(str(random.randint(100, 200)))