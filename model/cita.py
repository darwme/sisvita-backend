from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cita(db.Model):
    __tablename__ = 'cita'
    id_cita = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    fecha_agenda = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.String(50), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)

    especialista = db.relationship('Especialista', backref=db.backref('citas', lazy=True))
    paciente = db.relationship('Paciente', backref=db.backref('citas', lazy=True))

    def __init__(self, id_especialista, id_paciente, fecha_agenda, estado, motivo):
        self.id_especialista = id_especialista
        self.id_paciente = id_paciente
        self.fecha_agenda = fecha_agenda
        self.estado = estado
        self.motivo = motivo
