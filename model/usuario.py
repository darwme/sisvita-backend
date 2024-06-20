from utils.db import db
from sqlalchemy import Enum
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    clave = db.Column(db.String(8))

    def __init__(self,email,clave):
        self.email = email
        self.clave = clave



