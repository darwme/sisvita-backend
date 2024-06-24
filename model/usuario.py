from utils.db import db
from sqlalchemy import Enum
from dataclasses import dataclass

usuario_types = ('administrador','persona')
usuario_enum = Enum(*usuario_types, name='tipo_usuario')

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    clave = db.Column(db.String(250))
    tipo_usuario = db.Column(usuario_enum, default = 'persona')

    def __init__(self,email,clave, tipo_usuario):
        self.email = email
        self.clave = clave
        self.tipo_usuario = tipo_usuario



