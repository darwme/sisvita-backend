from utils.db import db
from datetime import date
from dataclasses import dataclass
from sqlalchemy import CheckConstraint, Enum


sexo_types = ('M', 'F')
sexo_enum = Enum(*sexo_types, name='sexo')
estado_civil_types = ('S', 'C', 'D', 'V', 'U')
estado_civil_enum = Enum(*estado_civil_types, name='estado_civil')

tipo_usuario_types = ('especialista', 'estudiante')
tipo_usuario_enum = Enum(*tipo_usuario_types, name='tipo_usuario')

@dataclass
class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(128))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(sexo_enum, nullable=False)
    estado_civil = db.Column(estado_civil_enum, nullable=False)
    tipo_usuario = db.Column(tipo_usuario_enum, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, nombre, apellido, email, clave, fecha_nacimiento=None, sexo=None, estado_civil=None, tipo_usuario=None, is_admin=False):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.is_admin = is_admin
        self.tipo_usuario = tipo_usuario

    