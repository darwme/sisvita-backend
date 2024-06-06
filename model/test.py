from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__='test'
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    clasificacion= db.Column(db.String(100))
    total_test = db.Column(db.Integer)
    fecha = db.Column(db.Date)

    estudiante = db.relationship('Estudiante', backref='tests')
    
    def __init__(self, id_estudiante, clasificacion, total_test, fecha):
        self.id_estudiante = id_estudiante
        self.clasificacion = clasificacion
        self.total_test = total_test
        self.fecha = fecha