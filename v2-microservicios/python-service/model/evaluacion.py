from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Evaluacion(db.Model):
    __tablename__ = 'evaluacion'
    id_evaluacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    id_historial_test = db.Column(db.Integer, db.ForeignKey('historial_test.id_historial_test'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    fecha_evaluacion = db.Column(db.DateTime)
    fundamento_cientifico = db.Column(db.String(250))
    tratamiento = db.Column(db.String(255))
    descripcion_tratamiento = db.Column(db.String(500))
    comunicacion = db.Column(db.String(500))

    especialista = db.relationship('Especialista', backref='evaluaciones')
    historial_test = db.relationship('Historial_test', backref='evaluacion')
    paciente = db.relationship('Paciente', backref='evaluaciones')

    def __init__(self, id_especialista, id_historial_test, id_paciente, fecha_evaluacion, fundamento_cientifico, tratamiento, descripcion_tratamiento, comunicacion):
        self.id_especialista = id_especialista
        self.id_historial_test = id_historial_test
        self.id_paciente = id_paciente
        self.fecha_evaluacion = fecha_evaluacion
        self.fundamento_cientifico = fundamento_cientifico
        self.tratamiento = tratamiento
        self.descripcion_tratamiento = descripcion_tratamiento
        self.comunicacion = comunicacion
