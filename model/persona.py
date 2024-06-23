from utils.db import db
from dataclasses import dataclass
from sqlalchemy import Enum

sexo_types = ('masculino', 'femenino')
sexo_enum = Enum(*sexo_types, name='sexo')
estado_civil_types = ('soltero', 'casado', 'divorciado', 'viudo')
estado_civil_enum = Enum(*estado_civil_types, name='estado_civil')

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_ubicacion = db.Column(db.Integer, db.ForeignKey('ubicacion.id_ubicacion'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(sexo_enum)
    estado_civil = db.Column(estado_civil_enum)
    celular = db.Column(db.String(9))
    
    usuario = db.relationship('Usuario', backref='persona')
    ubicacion = db.relationship('Ubicacion', backref='ubicacion')

    def __init__(self, id_ubicacion, id_usuario, nombres, apellidos,fecha_nacimiento, sexo, estado_civil,celular):
        self.id_ubicacion = id_ubicacion
        self.id_usuario = id_usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.celular = celular
