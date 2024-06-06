from utils.db import db
from dataclasses import dataclass

@dataclass
class Situacion(db.Model):
    __tablename__ = 'situacion'
    id_situacion = db.Column(db.Integer, primary_key=True)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'))
    enunciado = db.Column(db.String(255))

    seccion = db.relationship('Seccion', backref='situacion')

    def __init__(self, id_seccion, enunciado):
        self.id_seccion = id_seccion
        self.enunciado = enunciado
