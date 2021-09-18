class Config:
    SECRET_KEY = 'super_secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mauro:mauro9812@localhost/flaskmysql'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'



