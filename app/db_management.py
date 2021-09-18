from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    mail = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, name, lastname, mail,username, password):
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.username = username
        self.password = password


class TaskSchema(ma.Schema):

    class Meta:
        fields = ('username', 'name')


def init_db():
    task_schema = TaskSchema()
    tasks_schema = TaskSchema(many=True)


def add_user(name, lastname, mail, username, password_hash):
    new_task = User(name, lastname, mail, username, password_hash)
    db.session.add(new_task)
    db.session.commit()

def get_user(username):
    user = User.query.filter_by(username=username).first()
    return user