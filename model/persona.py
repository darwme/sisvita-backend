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
    dni = db.Column(db.String(8))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(sexo_enum)
    estado_civil = db.Column(estado_civil_enum)
    num_celular = db.Column(db.String(9))
    
    usuario = db.relationship('Usuario', backref='persona')

    def __init__(self, id_usuario, nombres, apellidos,dni,fecha_nacimiento, sexo, estado_civil,num_celular):
        self.id_usuario = id_usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.num_celular = num_celular
