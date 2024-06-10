from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuestionario(db.Model):
    __tablename__ = 'cuestionario'
    id_cuestionario = db.Column(db.Integer, primary_key=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'))
    total_cuestionario = db.Column(db.Integer)

    seccion = db.relationship('Seccion', backref='cuestionarios')
    test = db.relationship('Test', backref='cuestionarios')

    def __init__(self, id_cuestionario, id_test, id_seccion, total_cuestionario):
        self.id_cuestionario = id_cuestionario
        self.id_test = id_test
        self.id_seccion = id_seccion
        self.total_cuestionario = total_cuestionario