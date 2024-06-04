from utils.db import db
from dataclasses import dataclass

@dataclass
class Seccion(db.Model):
    __tablename__='seccion'
    id_seccion= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    
    def __init__(self,id_seccion,nombre):
        self.id_seccion = id_seccion
        self.nombre = nombre
        pass