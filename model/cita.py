from utils.db import db
from dataclasses import dataclass
from datetime import datetime

#FALTA
#estadoType = ('pendiente','atendido','cancelado')
#estado_enum = Enum(*estadoType, name='estado_cita')

@dataclass
class Cita(db.Model):
    __tablename__ = 'cita'
    id_cita = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    fecha_agenda = db.Column(db.DateTime)
    estado = db.Column(db.String(50))
    motivo = db.Column(db.String(255))
    hora = db.Column(db.Time)
    
    especialista = db.relationship('Especialista', backref='citas')
    paciente = db.relationship('Paciente', backref='citas')
    

    def __init__(self, id_especialista, id_paciente, fecha_agenda, estado, motivo,hora):
        self.id_especialista = id_especialista
        self.id_paciente = id_paciente
        self.fecha_agenda = fecha_agenda
        self.estado = estado
        self.motivo = motivo
        self.hora = hora
