from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    __tablename__='pregunta'
    id_pregunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_situacion = db.Column(db.Integer, db.ForeignKey('situacion.id_situacion'))
    descripcion = db.Column(db.String(250))
    
    situacion = db.relationship('Situacion', backref='preguntas')

    def __init__(self,id_situacion,descripcion):
        self.id_situacion = id_situacion
        self.descripcion = descripcion