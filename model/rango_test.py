from utils.db import db
from dataclasses import dataclass

@dataclass
class Rango_test(db.Model):
    __tablename__='rango_test'
    id_rango_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    diagnostico = db.Column(db.String(100))
    
    test = db.relationship('Test', backref='rango_test')

    def __init__(self,id_test,minimo,maximo,diagnostico):
        self.id_test= id_test
        self.minimo = minimo
        self.maximo = maximo
        self.diagnostico = diagnostico
