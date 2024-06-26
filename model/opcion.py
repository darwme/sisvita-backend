from utils.db import db
from dataclasses import dataclass

@dataclass
class Opcion(db.Model):
    __tablename__='opcion'
    id_opcion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    descripcion = db.Column(db.String(50))
    valor_opcion = db.Column(db.Integer)
    
    test = db.relationship('Test', backref='opciones')

    def __init__(self,id_test,descripcion,valor_opcion):
        self.id_test = id_test
        self.descripcion = descripcion
        self.valor_opcion = valor_opcion