from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(db.String(1))
    estado_civil = db.Column(db.String(1))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, nombre, apellido, email, clave, fecha_nacimiento=None, sexo=None, estado_civil=None, is_admin=False):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.is_admin = is_admin
