from utils.db import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__='test'
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    cant_secciones = db.Column(db.Integer)
        
    def __init__(self, nombre,cant_secciones):
        self.nombre = nombre
        self.cant_secciones = cant_secciones