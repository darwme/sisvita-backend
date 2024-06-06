from utils.db import db
from dataclasses import dataclass

@dataclass
class Clasificacion(db.Model):
    __tablename__ = 'clasificacion'
    id_clasificacion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    sexo = db.Column(db.String(1))

    def __init__(self, id_clasificacion, nombre, categoria, minimo, maximo, sexo):
        self.id_clasificacion = id_clasificacion
        self.nombre = nombre
        self.categoria = categoria
        self.minimo = minimo
        self.maximo = maximo
        self.sexo = sexo
