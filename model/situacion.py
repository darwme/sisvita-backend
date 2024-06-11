from utils.db import db
from dataclasses import dataclass

@dataclass
class Situacion(db.Model):
    __tablename__ = 'situacion'
    id_situacion = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(255))

    def __init__(self, id_situacion, enunciado):
        self.id_situacion = id_situacion
        self.enunciado = enunciado

def crear_situaciones():
    secciones = ['cognitivo', 'fisiologico', 'motor']
    enunciados = [
        'enunciado 1', 'enunciado 2', 'enunciado 3', 'enunciado 4', 'enunciado 5',
        'enunciado 6', 'enunciado 7', 'enunciado 8', 'enunciado 9', 'enunciado 10',
        'enunciado 11', 'enunciado 12', 'enunciado 13', 'enunciado 14', 'enunciado 15',
        'enunciado 16', 'enunciado 17', 'enunciado 18', 'enunciado 19', 'enunciado 20',
        'enunciado 21', 'enunciado 22', 'enunciado 23']
    
    id_situacion = 1
    for seccion in secciones:
        for enunciado in enunciados:
            situacion = Situacion.query.get(id_situacion)
            if not situacion:
                new_situacion = Situacion(id_situacion=id_situacion, seccion=seccion, enunciado=enunciado)
                db.session.add(new_situacion)
            id_situacion += 1

    db.session.commit()
    print('Situaciones creadas o ya existentes.')
