from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id_pregunta = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(255))

    def __init__(self, id_pregunta, enunciado):
        self.id_pregunta = id_pregunta
        self.enunciado = enunciado
