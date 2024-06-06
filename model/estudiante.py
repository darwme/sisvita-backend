from utils.db import db
from dataclasses import dataclass
from model.test import Test

@dataclass
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id_estudiante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    codigo_estudiante = db.Column(db.Integer)
    carrera_profesional = db.Column(db.String(50))

    usuario = db.relationship('Usuario', backref='estudiante')

    def __init__(self, id_usuario, codigo_estudiante, carrera_profesional):
        self.id_usuario = id_usuario
        self.codigo_estudiante = codigo_estudiante
        self.carrera_profesional = carrera_profesional


    def getTests(self):
        return Test.query.filter_by(id_estudiante=self.id_estudiante).all()
    
    def getTestByIdEstudiante(self, id_test):
        return Test.query.filter_by(id_test=id_test, id_estudiante=self.id_estudiante).first()