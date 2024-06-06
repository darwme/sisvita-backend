from utils.db import db
from dataclasses import dataclass

@dataclass
class Fila(db.Model):
    __tablename__ = 'fila'
    id_fila = db.Column(db.Integer, primary_key=True)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'))
    id_situacion = db.Column(db.Integer, db.ForeignKey('situacion.id_situacion'))

    pregunta = db.relationship('Pregunta', backref='filas')
    situacion = db.relationship('Situacion', backref='filas')

    def __init__(self, id_fila, id_pregunta, id_situacion):
        self.id_fila = id_fila
        self.id_pregunta = id_pregunta
        self.id_situacion = id_situacion
