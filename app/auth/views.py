from flask import render_template, session, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import csrf

from app.db_management import add_user, get_user
from app.forms import LoginForm, SignupForm
from . import auth
from app.models import UserModel, UserData


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    # Esta funcion detecta que el método es POST y que el formulario es valido,
    # cuando esto suceda entonces se ejecutará la función
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_obj = get_user(username)

        if user_obj is not None:
            password_from_db = user_obj.password

            if check_password_hash(password_from_db, password):
                """Se usa compare_digest porque evita los ataques de tiempos
                Es decir, no revela informacion por el tiempo de comparacion"""
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido de nuevo')
                return redirect(url_for('dashboard'))
            else:
                flash('Informacion no coicide 0')
        else:
            flash('Informacion no coicide 1')
        
        return redirect(url_for('auth.login'))

    return render_template('login.html', **context)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')
    return redirect(url_for('haven'))


@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()

    context = {
        'signup_form': signup_form
    }
    if signup_form.validate_on_submit():
        """Debe verificarse si ya existe ese nombre de usuario para no 
        causar problemas en la base de datos"""

        name = signup_form.name.data
        lastname = signup_form.lastname.data
        mail = signup_form.mail.data
        username = signup_form.username.data
        password = signup_form.password.data
        password_hash = generate_password_hash(password)
        response = add_user(name, lastname, mail, username, password_hash)
        if response == 1:
            flash('Usuario o correo ya existe')
            redirect(url_for('auth.login'))
        else:
            user_data = UserData(username, password_hash)
            user = UserModel(user_data)
            login_user(user)

            flash('Usuario agregado correctamente')
            return redirect(url_for('dashboard'))

    return render_template('signup.html', **context)
