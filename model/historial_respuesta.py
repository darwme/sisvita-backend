from utils.db import db
from dataclasses import dataclass

@dataclass
class Historial_respuesta(db.Model):
    __tablename__ = 'historial_respuesta'
    id_historial_test = db.Column(db.Integer, db.ForeignKey('historial_test.id_historial_test'), primary_key=True)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'), primary_key=True)
    
    historial_test = db.relationship('Historial_test', backref=db.backref('historiales_respuestas', cascade='all, delete-orphan'))
    pregunta = db.relationship('Pregunta', backref=db.backref('historiales_respuestas', cascade='all, delete-orphan'))
    
    def __init__(self, id_historial_test, id_pregunta):
        self.id_historial_test = id_historial_test
        self.id_pregunta = id_pregunta
