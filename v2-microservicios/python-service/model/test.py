from utils.db import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__='test'
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(250))
        
    def __init__(self, nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion