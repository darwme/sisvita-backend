from utils.db import db
from dataclasses import dataclass

@dataclass
class Situacion(db.Model):
    __tablename__ = 'situacion'
    id_situacion = db.Column(db.Integer, primary_key=True)
    seccion = db.Column(db.String(255))
    enunciado = db.Column(db.String(255))

    def __init__(self, id_situacion, seccion, enunciado):
        self.id_situacion = id_situacion
        self.seccion = seccion
        self.enunciado = enunciado
