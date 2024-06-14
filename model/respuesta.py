from utils.db import db
from dataclasses import dataclass
from sqlalchemy import CheckConstraint, Enum

    
@dataclass
class Respuesta(db.Model):
    __tablename__='respuesta'
    id_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_fila = db.Column(db.Integer, db.ForeignKey('fila.id_fila'), nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    valor = db.Column(db.Integer)
    
    fila = db.relationship('Fila', backref='respuestas')
    test = db.relationship('Test', backref='respuestas')
    
    def __init__(self, id_fila,id_test,valor):
        self.id_fila = id_fila
        self.id_test = id_test
        self.valor = valor
        
