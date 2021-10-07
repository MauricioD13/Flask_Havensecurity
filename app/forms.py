from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Clase que permite usar la extension de flask WTF para el
    uso de formularios
    Args:
        FlaskForm ([class]): Clase padre que se importa desde la extension
    """
    username = StringField('Nombre de usuario: ', validators=[DataRequired()])
    password = PasswordField('Contraseña: ', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class SignupForm(FlaskForm):
    name = StringField('Nombres:', validators=[DataRequired()])
    lastname = StringField('Apellidos:', validators=[DataRequired()])
    mail = StringField('Correo:', validators=[DataRequired()])
    username = StringField('Nombre de usuario: ', validators=[DataRequired()])
    password = PasswordField('Contraseña: ', validators=[DataRequired()])
    submit = SubmitField('Enviar')


