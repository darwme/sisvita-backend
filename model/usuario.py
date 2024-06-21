from utils.db import db
from sqlalchemy import Enum
from dataclasses import dataclass

usuario_types = ('administrador','paciente', 'especialista', 'mixto')
usuario_enum = Enum(*usuario_types, name='tipo_usuario')

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    clave = db.Column(db.String(250))
    tipo_usuario = db.Column(usuario_enum)

    def __init__(self,email,clave):
        self.email = email
        self.clave = clave



