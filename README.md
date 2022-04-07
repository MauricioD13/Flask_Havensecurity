# Flask Havensecurity
Aplicacion web para el proyecto de IoT. Esta aplicación se hizo en el framework Flask, con las dependencias de:
- SQLAlchemy: Debido a que Flask no tiene un ORM por defecto se usa este paquete para el manejo de las bases de datos
- Flask-WTF: Este paquete se usa para el manejo de formularios 
- Flask-Login: Proceso de Login y Logout
- Flask-Bootstrap: Uso del framework Frontend de Bootstrap
- gunicorn: Necesario para poder llevar la app a la nube de Heroku
### Estructura
main.py: Rutas y logico general de la aplicación 
App ->
  - auth: Contiene todos los archivos necesarios para la autenticacion y registro
  - static: Archivos estáticos, es decir, archivos de CSS y las imagenes usadas
  - templates: Archivos HTML que son usados en cada vista
  - forms.py: Contiene todos los formularios
  - models.py: Modelos usados para guardar los datos en la base de datos
  - db_management.py: Inicializacion del ORM y manejo de los datos
