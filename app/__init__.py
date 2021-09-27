from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .config import Config_development, Config_production
from .auth import auth
from .models import UserModel
from .db_management import db, ma

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    """Cada vez que flask quiera cargar el usuario
    para la sesion activa llamara esta funcion de query"""
    return UserModel.query(username)


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)  #Inicializacion de la extension bootstrap
    # Ya se tiene acceso a los archivos HTML, CSS y JS

    app.config.from_object(Config_production)  # Necesario para hacer uso de la sesion

    db.init_app(app)

    ma.init_app(app)

    login_manager.init_app(app)  #Inicializar el administrador de logins en la app

    app.register_blueprint(auth)

    return app, db, ma

