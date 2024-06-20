from utils.db import db
from dataclasses import dataclass
from datetime import date

@dataclass
class Historial_test(db.Model):
    __tablename__='historial_test'
    id_historial_test = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    test_realizado = db.Column(db.String(50))
    fecha_realizada = db.Column(db.Date)
    cant_preguntas_realizadas = db.Column(db.Integer)
    puntaje_realizado = db.Column(db.Integer)
    diagnostico = db.Column(db.String(50))
    
    usuario = db.relationship('Usuario', backref='historiales_tests')


    def __init__(self,id_usuario,test_realizado,fecha_realizada,cant_preguntas_realizadas,puntaje_realizado,diagnostico):
        self.id_usuario = id_usuario
        self.test_realizado = test_realizado
        self.fecha_realizada = fecha_realizada
        self.cant_preguntas_realizadas = cant_preguntas_realizadas
        self.puntaje_realizado = puntaje_realizado
        self.diagnostico = diagnostico
