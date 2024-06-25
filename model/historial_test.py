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
    puntaje_realizado = db.Column(db.String(250))
    diagnosticos = db.Column(db.String(50))
    
    usuario = db.relationship('Usuario', backref='historiales_usuarios')
    test = db.relationship('Test', backref='historiales_tests')


    def __init__(self,id_usuario,id_test,fecha_realizada,puntaje_realizado,array_diagnostico):
        self.id_usuario = id_usuario
        self.id_test = id_test
        self.fecha_realizada = fecha_realizada
        self.puntaje_realizado = puntaje_realizado
        self.diagnosticos = diagnosticos
