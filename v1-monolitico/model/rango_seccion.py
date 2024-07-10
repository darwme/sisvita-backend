from utils.db import db
from dataclasses import dataclass

@dataclass
class Rango_seccion(db.Model):
    __tablename__='rango_seccion'
    id_rango_seccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'))
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    diagnostico = db.Column(db.String(250))
    
    test = db.relationship('Seccion', backref='rango_seccion')

    def __init__(self,id_seccion,minimo,maximo,diagnostico):
        self.id_seccion= id_seccion
        self.minimo = minimo       
        self.maximo = maximo
        self.diagnostico = diagnostico
