from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuesta(db.Model):
    __tablename__='respuesta'
    id_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_historial_test = db.Column(db.Integer, db.ForeignKey('historial_test.id_historial_test'))
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'))
    valor = db.Column(db.Integer)
    
    historial_test = db.relationship('Historial_test', backref='respuestas')
    pregunta = db.relationship('Pregunta', backref='respuestas')

    def __init__(id_historial_test,self,id_pregunta,valor):
        self.id_historial_test = id_historial_test
        self.id_pregunta = id_pregunta
        self.valor = valor