from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    codigo_especialista = db.Column(db.String(8))
    especialidad = db.Column(db.String(50))
    experiencia = db.Column(db.Integer)

    persona = db.relationship('Persona', backref='especialista')

    def __init__(self, id_persona, codigo_especialista, especialidad, experiencia):
        self.id_persona = id_persona
        self.codigo_especialista = codigo_especialista
        self.especialidad = especialidad
        self.experiencia = experiencia

