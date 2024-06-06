from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Test_isra(db.Model):
    __tablename__='test_isra'
    id_test_isra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    fecha = db.Column(db.Date)
    punt_test = db.Column(db.Integer)

    estudiante = db.relationship('Estudiante', backref='tests')
    
    def __init__(self,id_test_isra, id_estudiante, fecha, punt_test):
        self.id_test_isra = id_test_isra
        self.id_estudiante = id_estudiante
        self.fecha = fecha
        self.punt_test = punt_test
