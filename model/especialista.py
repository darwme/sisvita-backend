from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    codigo_especialista = db.Column(db.String(100), nullable=False, unique=True)
    especialidad = db.Column(db.String(100), nullable=False)
    experiencia = db.Column(db.String(255))

    persona = db.relationship('Persona', backref=db.backref('especialistas', lazy=True))

    def __init__(self, id_persona, codigo_especialista, especialidad, experiencia):
        self.id_persona = id_persona
        self.codigo_especialista = codigo_especialista
        self.especialidad = especialidad
        self.experiencia = experiencia
