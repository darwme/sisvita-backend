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
from services.gestor_ubicacion import gestor_ubicacion
from services.historial_test import historial_test
from services.seccion_respuesta import seccion_respuesta
from services.test import test
from services.rango_test import rango_test
from services.rango_seccion import rango_seccion
from services.opcion import opcion
from services.seccion import seccion
from services.situacion import situacion
from services.pregunta import pregunta

from services.gestor_auth import gestor_auth
from services.gestor_evaluacion import gestor_evaluacion
from services.gestor_historial_test import gestor_historial_test
from services.gestor_profile import gestor_profile
from services.gestor_realizar_test import gestor_realizar_test
from services.gestor_test import gestor_test
from services.gestor_ubicacion import gestor_ubicacion


#model
from model.ubicacion import Ubicacion


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

app.register_blueprint(gestor_auth)
app.register_blueprint(gestor_evaluacion)
app.register_blueprint(gestor_historial_test)
app.register_blueprint(gestor_profile)
app.register_blueprint(gestor_realizar_test)
app.register_blueprint(gestor_test)
app.register_blueprint(gestor_ubicacion)

with app.app_context():
    db.create_all()
    Ubicacion.upload_ubicacion_peru()

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
