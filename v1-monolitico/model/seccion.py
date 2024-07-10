from utils.db import db
from dataclasses import dataclass

@dataclass
class Seccion(db.Model):
    __tablename__='seccion'
    id_seccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    descripcion = db.Column(db.String(250))
    
    test = db.relationship('Test', backref='secciones')

    def __init__(self,id_test,descripcion):
        self.id_test = id_test
        self.descripcion = descripcion