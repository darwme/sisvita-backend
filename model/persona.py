from utils.db import db
from dataclasses import dataclass
from sqlalchemy import Enum

sexo_types = ('M', 'F')
sexo_enum = Enum(*sexo_types, name='sexo')
estado_civil_types = ('S', 'C', 'D', 'V', 'U')
estado_civil_enum = Enum(*estado_civil_types, name='estado_civil')

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), unique=True, nullable=False)
    nombre = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    sexo = db.Column(sexo_enum, nullable=False)
    estado_civil = db.Column(estado_civil_enum, nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    celular = db.Column(db.String(9))

    paciente = db.relationship('Paciente', uselist=False, back_populates='persona')
    especialista = db.relationship('Especialista', uselist=False, back_populates='persona')
    usuario = db.relationship('Usuario', back_populates='persona')

    def __init__(self, id_usuario, nombre, apellidos, sexo, estado_civil, fecha_nacimiento):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.fecha_nacimiento = fecha_nacimiento

