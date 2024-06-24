from flask import Flask
from flask_jwt_extended import JWTManager 

#utils
from utils.db import db

#services
from services.administrador import administrador
from services.usuario import usuario
from services.persona import persona
from services.especialista import especialista
from services.paciente import paciente
from services.cita import cita
from services.ubicacion import ubicacion

from services.historial_test import historial_test
from services.seccion_respuesta import seccion_respuesta


from services.test import test
from services.rango_test import rango_test
from services.rango_seccion import rango_seccion
from services.opcion import opcion

from services.seccion import seccion
from services.situacion import situacion
from services.pregunta import pregunta

from services.auth import auth
from services.gestion_test import gestion_test


#model
from model.ubicacion import Ubicacion

from services.administrar import administrar

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
app.register_blueprint(administrador)
app.register_blueprint(usuario)
app.register_blueprint(persona)
app.register_blueprint(especialista)
app.register_blueprint(paciente)
app.register_blueprint(cita)

app.register_blueprint(historial_test)
app.register_blueprint(seccion_respuesta)

app.register_blueprint(test)
app.register_blueprint(rango_test)
app.register_blueprint(rango_seccion)
app.register_blueprint(opcion)

app.register_blueprint(seccion)
app.register_blueprint(situacion)
app.register_blueprint(pregunta)
app.register_blueprint(auth)
app.register_blueprint(administrar)
app.register_blueprint(ubicacion)
app.register_blueprint(gestion_test)


with app.app_context():
    db.create_all()
    Ubicacion.upload_ubicacion_peru()

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
