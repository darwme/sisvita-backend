from flask import Flask
from flask_jwt_extended import JWTManager 

#utils
from utils.db import db

#services
from services.seccion import seccion
from services.estudiante import estudiante
from services.test import test_routes
#from services.cuestionario import cuestionario
from services.especialista import especialista
from services.usuario import usuario_bp
from services.situacion import situacion
from services.pregunta import pregunta
from services.fila import fila
from services.clasificacion import clasificacion
from services.diagnostico import diagnostico
from services.respuesta import respuesta
from services.auth import auth

#model
from model.seccion import crear_secciones
from model.clasificacion import crear_clasificaciones

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app= Flask(__name__)
CORS(app, origins='*')
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Configuracion del JWT
app.config['SECRET_KEY'] = 'sisvita_secret_key'
app.config["JWT_SECRET_KEY"] = 'sisvita_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']


jwt = JWTManager(app)


#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(estudiante)
app.register_blueprint(test_routes)
#app.register_blueprint(cuestionario)
app.register_blueprint(especialista)
app.register_blueprint(usuario_bp)
app.register_blueprint(seccion)

app.register_blueprint(situacion)
app.register_blueprint(pregunta)
app.register_blueprint(fila)
app.register_blueprint(clasificacion)
app.register_blueprint(diagnostico)
app.register_blueprint(respuesta)

app.register_blueprint(auth)

with app.app_context():
    db.create_all()
    crear_secciones()
    crear_clasificaciones()

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
