from utils.db import db
from dataclasses import dataclass

@dataclass
class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    id_diagnostico = db.Column(db.Integer, primary_key=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    id_clasificacion = db.Column(db.Integer, db.ForeignKey('clasificacion.id_clasificacion'))
    categoria = db.Column(db.String(100))
    puntaje = db.Column(db.Integer)

    test = db.relationship('Test', backref='diagnostico')
    clasificacion = db.relationship('Clasificacion', backref='diagnostico')

    def __init__(self, id_diagnostico, id_test, id_clasificacion, categoria, puntaje):
        self.id_diagnostico = id_diagnostico
        self.id_test = id_test
        self.id_clasificacion = id_clasificacion
        self.categoria = categoria
        self.puntaje = puntaje
