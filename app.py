from flask import Flask,request, render_template,redirect, url_for
from dotenv import load_dotenv
from flask_login import LoginManager, login_required, login_user
from db import db
from models.user import User
from flask_restful import Api,Resource
import os

app = Flask(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

    secret_key = os.urandom(24)


# Configurar la base de datos u otras configuraciones
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = secret_key   
# Crear una instancia de SQLAlchemy como Singleton

api= Api(app)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    return None
with app.app_context():
        from Controllers.cuidador_perro_controller import CuidadorPerroController
        db.create_all()

        # Registrar blueprint del controlador
        # app.register_blueprint(Controlador)


# Ruta para mostrar la lista de perros
# Rutas
@app.route('/')
def index():
    return "Ingresé al sistema http://127.0.0.1:5000/login"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:

            login_user(user)
            return redirect(url_for("cuidadorperrocontroller"))

        
    return render_template("login.html")

# @app.route('/perros_mario')
# def perros_mario():
#     controlador = Controlador()  # Crear instancia del controlador
#     mensaje = Controlador.asignar_perros_a_mario('Mario')
#     return render_template('perros_mario.html', mensaje=mensaje)
api.add_resource(CuidadorPerroController,'/consulta_nombre')
if __name__ == '__main__':
    app.run(debug=True)
