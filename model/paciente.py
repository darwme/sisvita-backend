from utils.db import db
from dataclasses import dataclass

@dataclass
class Paciente(db.Model):
    __tablename__ = 'paciente'
    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    codigo_paciente = db.Column(db.String(100))
    antecedentes = db.Column(db.String(255))

    persona = db.relationship('Persona', backref='paciente')

    def __init__(self, id_persona, codigo_paciente, antecedentes):
        self.id_persona = id_persona
        self.codigo_paciente = codigo_paciente
        self.antecedentes = antecedentes

