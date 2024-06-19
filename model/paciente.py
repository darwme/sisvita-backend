from utils.db import db
from dataclasses import dataclass

@dataclass
class Paciente(db.Model):
    __tablename__ = 'paciente'
    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), unique=True, nullable=False)
    codigo_paciente = db.Column(db.String(100), nullable=False, unique=True)
    antecedentes = db.Column(db.String(255))

    persona = db.relationship('Persona', back_populates='paciente', uselist=False)
    citas = db.relationship('Cita', backref='paciente', lazy=True)

    def __init__(self, id_persona, codigo_paciente, antecedentes):
        self.id_persona = id_persona
        self.codigo_paciente = codigo_paciente
        self.antecedentes = antecedentes

