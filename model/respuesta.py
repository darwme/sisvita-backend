from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuesta(db.Model):
    __tablename__='respuesta'
    id_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'))
    valor = db.Column(db.Integer)
    
    pregunta = db.relationship('Pregunta', backref='respuestas')

    def __init__(self,id_pregunta,valor):
        self.id_pregunta = id_pregunta
        self.valor = valor