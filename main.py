import io

from flask import request, redirect, render_template, session, make_response
from flask_login import login_required, current_user
import base64
from io import BytesIO
from matplotlib.figure import Figure

from app import create_app
from app.db_management import init_db
import random

random.seed(0)

app, db, ma = create_app()

temp = {}
x_values = []
for i in range(5):
    aux = random.randint(1, 35)
    x_values.append(aux)
    temp[str(aux)] = '0' + str(random.randint(1, 30)) + '/' + '0' + str(random.randint(1, 12))

gas = {}
for i in range(5):
    gas[str(random.randint(300, 800))] = '0' + str(random.randint(1, 30)) + '/' + '0' + str(random.randint(1, 12))


with app.app_context():
    # Es necesario cargar el contexto de la aplicación  para poder crear las tablas
    db.create_all()
init_db()


@app.route('/')
def index():
    """Función que extrae la información de la IP del usuario

    Returns:
        Response: Respuesta html que redireccione a la ruta 'hello'
    """
    user_ip = request.remote_addr
    response = make_response(redirect('haven'))
    session['user_ip'] = user_ip
    return response


@app.route('/haven', methods=['GET', 'POST'])
def haven():
    """Método que se usa para:
    - Crear una sesion y guardar la ip del usuario 
    - Crear una instancia que contiene un formulario
    Returns:
        [method]:Pasar parametros por medio de un diccionario al html y renderizar HTML 
    """
    user_ip = session.get('user_ip')

    context = {
        'user_ip': user_ip
    }
    return render_template('haven.html', **context)


@app.route('/dashboard')
@login_required
def dashboard():
    username = current_user.id
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x_values)
    buf = BytesIO()
    fig.savefig(buf, format="png")


    context = {
        'temp': temp,
        'gas': gas,
        'username': username
    }
    return render_template('dashboard.html', **context)


"""
#Rutas dinamicas que cambian segun un parametro
@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_to_do(user_id=user_id, todo_id=todo_id)
    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>', methods = ['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_to_do(user_id, todo_id, done)
    return redirect(url_for('hello'))
"""


@app.errorhandler(404)  # Manejo de error de la pagina
def not_found(error):
    # El argumento indica el numero identificador del error HTTP
    return render_template('Error_404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('Error_500.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
