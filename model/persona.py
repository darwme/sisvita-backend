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
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    sexo = db.Column(sexo_enum)
    estado_civil = db.Column(estado_civil_enum)
    fecha_nacimiento = db.Column(db.Date)
    celular = db.Column(db.String(9))
    
    usuario = db.relationship('Usuario', backref='persona')

    def __init__(self, id_usuario, nombre, apellidos, sexo, estado_civil, fecha_nacimiento,celular):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.fecha_nacimiento = fecha_nacimiento
        self.celular = celular
