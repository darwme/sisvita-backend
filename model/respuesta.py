from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuesta(db.Model):
    __tablename__ = 'respuesta'
    id_respuesta = db.Column(db.Integer, primary_key=True)
    id_cuestionario = db.Column(db.Integer, db.ForeignKey('cuestionario.id_cuestionario'))
    id_fila = db.Column(db.Integer, db.ForeignKey('fila.id_fila'))
    valor = db.Column(db.Integer)

    cuestionario = db.relationship('Cuestionario', backref='respuesta')
    fila = db.relationship('Fila', backref='respuesta')

    def __init__(self, id_respuesta, id_cuestionario, id_fila, valor):
        self.id_respuesta = id_respuesta
        self.id_cuestionario = id_cuestionario
        self.id_fila = id_fila
        self.valor = valor
