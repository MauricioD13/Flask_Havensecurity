from flask import request, redirect, render_template, make_response
from flask_login import login_required, current_user


from io import BytesIO
from matplotlib.figure import Figure
import base64

from app import create_app
from app.forms import PhotoForm
from app.db_management import init_db
import random

random.seed(0)

app, db, ma = create_app()

ids = {}
gas = {}
temp = {}
temp_values = []
gas_values = []
for i in range(5):
    aux = random.randint(1, 35)
    temp_values.append(aux)
    temp[str(aux)] = '0' + str(random.randint(1, 30)) + '/' + '0' + str(random.randint(1, 12))


for i in range(5):
    aux = random.randint(300, 800)
    gas_values.append(aux)
    gas[str(aux)] = '0' + str(random.randint(1, 30)) + '/' + '0' + str(random.randint(1, 12))

for i in range(5):
    aux = random.randint(10000, 100000)
    ids[str(aux)] = i


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
    context = {
        'user_ip': '00'
    }
    return render_template('haven.html', **context)


@app.route('/dashboard_temp_gas')
@login_required
def dashboard_temp_gas():
    username = current_user.id
    fig = Figure()
    ax1, ax2 = fig.subplots(1,2)
    ax1.plot(temp_values)
    ax2.plot(gas_values)
    ax1.set_title('Temperatura')
    ax2.set_title('Gas')
    buf = BytesIO()
    fig.savefig(buf, format="png")
    graph = base64.b64encode(buf.getbuffer()).decode("ascii")
    context = {
        'temp': temp,
        'gas': gas,
        'username': username,
        'graph': graph

    }
    return render_template('dashboard_temp_gas.html', **context)

@app.route('/dashboard_rfid/<photo_id>', methods=['GET', 'POST'])
@login_required
def dashboard_rfid(photo_id):
    photo_form = PhotoForm()
    context = {
        'ids': ids,
        'photo_form': photo_form,
        'photo_url': 'images/industrial00.jpeg',
        'photo_id': photo_id
    }
    if photo_form.validate_on_submit():
        context['photo_url'] = 'images/industrial0'+photo_id+'.jpeg'
        return render_template('dashboard_rfid.html', **context)


    return render_template('dashboard_rfid.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)  # Manejo de error de la pagina
def not_found(error):
    # El argumento indica el numero identificador del error HTTP
    return render_template('Error_404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('Error_500.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
