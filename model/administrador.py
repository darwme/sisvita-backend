from utils.db import db
from dataclasses import dataclass

@dataclass
class Administrador(db.Model):
    __tablename__ = 'administrador'
    id_administrador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    nombre_admin = db.Column(db.String(50))

    usuario = db.relationship('Usuario', backref='administrador')

    def __init__(self, id_usuario, nombre_admin):
        self.id_usuario = id_usuario
        self.nombre_admin = nombre_admin

