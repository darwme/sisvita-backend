from utils.db import db
from dataclasses import dataclass

@dataclass
class Historial_respuesta(db.Model):
    __tablename__ = 'historial_respuesta'
    id_historial_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_historial_test = db.Column(db.Integer, db.ForeignKey('historial_test.id_historial_test'))
    id_respuesta = db.Column(db.Integer, db.ForeignKey('respuesta.id_respuesta'))
    
    historial_test = db.relationship('Historial_test', backref='historiales_respuestas')
    pregunta = db.relationship('Historial_test', backref='historiales_respuestas')
   
    def __init__(self, id_historial_test,id_respuesta):
        self.id_historial_test = id_historial_test
        self.id_respuesta = id_respuesta
