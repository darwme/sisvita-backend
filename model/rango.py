from utils.db import db
from dataclasses import dataclass

@dataclass
class Opcion(db.Model):
    __tablename__='rango'
    id_rango = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    diagnostico = db.Column(db.String(100))
    
    test = db.relationship('Test', backref='rangos')

    def __init__(self, nombre,minimo,maximo,diagnostico):
        self.nombre = nombre
        self.minimo = minimo       
        self.maximo = maximo
        self.diagnostico = diagnostico
