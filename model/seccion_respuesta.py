from utils.db import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import ARRAY


@dataclass
class Seccion_respuesta(db.Model):
    __tablename__='seccion_respuesta'
    id_seccion_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('test.id_usuario'))   
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    id_seccion = db.Column(db.Integer, db.ForeignKey('test.id_seccion'))
    respuestas =db.Column(db.ARRAY(db.Integer))
    
    usuario = db.relationship('Usuario', backref='seccion_respuestas')   
    test = db.relationship('Test', backref='seccion_respuestas')
    seccion = db.relationship('Seccion', backref='seccion_respuestas')

    def __init__(self,id_usuario,id_test,id_seccion,respuestas):
        self.id_usuario = id_usuario
        self.id_test = id_test
        self.id_seccion = id_seccion
        self.respuestas = respuestas