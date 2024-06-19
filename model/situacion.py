from utils.db import db
from dataclasses import dataclass

@dataclass
class Situacion(db.Model):
    __tablename__='situacion'
    id_situacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'))
    descripcion = db.Column(db.String(250))
    cant_preguntas = db.Column(db.Integer)
    
    seccion = db.relationship('Seccion', backref='situaciones')

    def __init__(self,id_seccion,descripcion,cant_preguntas):
        self.id_seccion = id_seccion
        self.descripcion = descripcion
        self.cant_preguntas = cant_preguntas