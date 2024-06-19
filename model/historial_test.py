from utils.db import db
from dataclasses import dataclass
from datetime import date

@dataclass
class Historial_test(db.Model):
    __tablename__='historial_test'
    id_historial_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    fecha_realizada = db.Column(db.Date)
    puntaje_realizado = db.Column(db.Integer)
    diagnostico = db.Column(db.String(50))
    cant_preguntas_realizadas = db.Column(db.Integer)
    
    usuario = db.relationship('Usuario', backref='Historiales_tests')
    test = db.relationship('Test', backref='Historiales_tests')

    def __init__(self,id_usuario,id_test,fecha_realizada,puntaje_realizado,diagnostico,cant_preguntas_realizadas):
        self.id_usuario = id_usuario
        self.id_test = id_test
        self.fecha_realizada = fecha_realizada
        self.puntaje_realizado = puntaje_realizado
        self.diagnostico = diagnostico
        self.cant_preguntas_realizadas = cant_preguntas_realizadas
