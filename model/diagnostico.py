from utils.db import db
from dataclasses import dataclass
from sqlalchemy import CheckConstraint, Enum

categoria_types = ('cognitivo', 'fisiologico','motor','general')
categoria_enum = Enum(*categoria_types, name='categoria')
    
@dataclass
class Diagnostico(db.Model):
    __tablename__='diagnostico'
    id_diagnostico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    categoria = db.Column(categoria_enum, nullable=False)
    puntaje = db.Column(db.Integer)
    id_clasificacion = db.Column(db.Integer, db.ForeignKey('clasificion.id_clasificion'), nullable=False)
    
    test = db.relationship('Test', backref='diagnosticos')
    clasificacion = db.relationship('Clasificacion', backref='diagnosticos')
    
    def __init__(self, id_test,categoria,puntaje,id_clasificacion):
        self.id_test = id_test
        self.categoria = categoria
        self.puntaje = puntaje
        self.id_clasificacion = id_clasificacion
        
