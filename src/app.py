from flask import Flask 
from utils.db import db
from services.seccion import seccion
from services.estudiante import estudiante
from services.test import test_routes
from services.cuestionario import cuestionario
from services.especialista import especialista
from services.usuario import usuario_bp
from services.auth import auth

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(estudiante)
app.register_blueprint(test_routes)
app.register_blueprint(cuestionario)
app.register_blueprint(especialista)
app.register_blueprint(usuario_bp)
app.register_blueprint(seccion)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
