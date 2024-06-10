from utils.db import db
from dataclasses import dataclass

@dataclass
class Clasificacion(db.Model):
    __tablename__='clasificacion'
    id_clasificacion= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    
    def __init__(self,id_clasificacion,nombre):
        self.id_clasificacion = id_clasificacion
        self.nombre = nombre

def crear_secciones():
    clasificaciones = [
        {'id_clasificacion': 1, 'nombre': 'ansiedad minima'},
        {'id_clasificacion': 2, 'nombre': 'ansiedad moderada'},
        {'id_clasificacion': 3, 'nombre': 'ansiedad severa'},
        {'id_clasificacion': 4, 'nombre': 'ansiedad extrema'}
    ]

    for clasificacion_data in clasificaciones:
        clasificacion = Clasificacion.query.get(clasificacion_data['id_clasificacion'])
        if not clasificacion:
            new_clasificacion = Clasificacion(**clasificacion_data)
            db.session.add(new_clasificacion)

    db.session.commit()
    print('Secciones creadas o ya existentes.')