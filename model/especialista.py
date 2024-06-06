from utils.db import db

from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    especialidad = db.Column(db.String)

    usuario = db.relationship('Usuario', backref='especialista')    

    def __init__(self, id_usuario, especialidad):
        self.id_usuario = id_usuario
        self.especialidad = especialidad