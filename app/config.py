class Config:
    SECRET_KEY = 'super_secret'
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mauro:mauro9812@localhost/flaskmysql'
    SLQALCHEMY_DATABASE_URI = 'postgres://ndndythzfvhrca:16f8ba0ff2386ad7d03df7d5866ada2b216ae336043b0b69abf5df6db40488bb@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d3npmpir4tem4k'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'



