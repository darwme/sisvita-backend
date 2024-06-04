from utils.db import db
from dataclasses import dataclass

@dataclass
class Seccion(db.Model):
    __tablename__='seccion'
    id_seccion= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    
    def __init__(self,id_seccion,nombre):
        self.id_seccion = id_seccion
        self.nombre = nombre

def crear_secciones():
    secciones = [
        {'id_seccion': 1, 'nombre': 'cognitivo'},
        {'id_seccion': 2, 'nombre': 'fisiologico'},
        {'id_seccion': 3, 'nombre': 'motor'}
    ]

    for seccion_data in secciones:
        seccion = Seccion.query.get(seccion_data['id_seccion'])
        if not seccion:
            new_seccion = Seccion(**seccion_data)
            db.session.add(new_seccion)

    db.session.commit()
    print('Secciones creadas o ya existentes.')





    


