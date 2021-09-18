from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
#El prefijo se usa para rutear todas las peticiones que comiencen 
#con auth

from . import views
"""Se debe importar en esta parte
    Despues de crear el blueprint se importan las vistas
    que serán usadas en la aplicación 
"""


