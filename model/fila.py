from utils.db import db
from dataclasses import dataclass


@dataclass
class Fila(db.Model):
    __tablename__ = 'fila'
    id_fila = db.Column(db.Integer, primary_key=True)
    id_pregunta = db.Column(db.Integer)
    id_situacion = db.Column(db.Integer)
    
    def __init__(self, id_fila, id_pregunta, id_situacion):
        self.id_fila = id_fila
        self.id_pregunta = id_pregunta
        self.id_situacion = id_situacion


def crear_filas():
    filas = [
        {'id_fila': 1, 'id_pregunta': 1, 'id_situacion': 1},
        {'id_fila': 2, 'id_pregunta': 6, 'id_situacion': 1},
        {'id_fila': 3, 'id_pregunta': 1, 'id_situacion': 2},
        {'id_fila': 4, 'id_pregunta': 4, 'id_situacion': 3},
        {'id_fila': 5, 'id_pregunta': 6, 'id_situacion': 3},
        {'id_fila': 6, 'id_pregunta': 1, 'id_situacion': 4},
        {'id_fila': 7, 'id_pregunta': 6, 'id_situacion': 4},
        {'id_fila': 8, 'id_pregunta': 3, 'id_situacion': 5},
        {'id_fila': 9, 'id_pregunta': 4, 'id_situacion': 5},
        {'id_fila': 10, 'id_pregunta': 1, 'id_situacion': 6},
        {'id_fila': 11, 'id_pregunta': 2, 'id_situacion': 6},
        {'id_fila': 12, 'id_pregunta': 4, 'id_situacion': 6},
        {'id_fila': 13, 'id_pregunta': 7, 'id_situacion': 6},
        {'id_fila': 14, 'id_pregunta': 4, 'id_situacion': 7},
        {'id_fila': 15, 'id_pregunta': 2, 'id_situacion': 8},
        {'id_fila': 16, 'id_pregunta': 7, 'id_situacion': 8},
        {'id_fila': 17, 'id_pregunta': 6, 'id_situacion': 9},
        {'id_fila': 18, 'id_pregunta': 7, 'id_situacion': 9},
        {'id_fila': 19, 'id_pregunta': 1, 'id_situacion': 10},
        {'id_fila': 20, 'id_pregunta': 4, 'id_situacion': 10},
        {'id_fila': 21, 'id_pregunta': 6, 'id_situacion': 10},
        {'id_fila': 22, 'id_pregunta': 7, 'id_situacion': 10},
        {'id_fila': 23, 'id_pregunta': 6, 'id_situacion': 11},
        {'id_fila': 24, 'id_pregunta': 3, 'id_situacion': 12},
        {'id_fila': 25, 'id_pregunta': 5, 'id_situacion': 12},
        {'id_fila': 26, 'id_pregunta': 6, 'id_situacion': 12},
        {'id_fila': 27, 'id_pregunta': 4, 'id_situacion': 13},
        {'id_fila': 28, 'id_pregunta': 5, 'id_situacion': 13},
        {'id_fila': 29, 'id_pregunta': 6, 'id_situacion': 13},
        {'id_fila': 30, 'id_pregunta': 7, 'id_situacion': 13},
        {'id_fila': 31, 'id_pregunta': 1, 'id_situacion': 14},
        {'id_fila': 32, 'id_pregunta': 5, 'id_situacion': 15},
        {'id_fila': 33, 'id_pregunta': 6, 'id_situacion': 16},
        {'id_fila': 34, 'id_pregunta': 1, 'id_situacion': 17},
        {'id_fila': 35, 'id_pregunta': 2, 'id_situacion': 17},
        {'id_fila': 36, 'id_pregunta': 5, 'id_situacion': 17},
        {'id_fila': 37, 'id_pregunta': 6, 'id_situacion': 17},
        {'id_fila': 38, 'id_pregunta': 7, 'id_situacion': 17},
        {'id_fila': 39, 'id_pregunta': 3, 'id_situacion': 18},
        {'id_fila': 40, 'id_pregunta': 6, 'id_situacion': 18},
        {'id_fila': 41, 'id_pregunta': 1, 'id_situacion': 19},
        {'id_fila': 42, 'id_pregunta': 2, 'id_situacion': 19},
        {'id_fila': 43, 'id_pregunta': 3, 'id_situacion': 19},
        {'id_fila': 44, 'id_pregunta': 5, 'id_situacion': 19},
        {'id_fila': 45, 'id_pregunta': 7, 'id_situacion': 19},
        {'id_fila': 46, 'id_pregunta': 1, 'id_situacion': 20},
        {'id_fila': 47, 'id_pregunta': 2, 'id_situacion': 20},
        {'id_fila': 48, 'id_pregunta': 5, 'id_situacion': 20},
        {'id_fila': 49, 'id_pregunta': 1, 'id_situacion': 21},
        {'id_fila': 50, 'id_pregunta': 2, 'id_situacion': 21},
        {'id_fila': 51, 'id_pregunta': 3, 'id_situacion': 21},
        {'id_fila': 52, 'id_pregunta': 4, 'id_situacion': 21},
        {'id_fila': 53, 'id_pregunta': 5, 'id_situacion': 21},
        {'id_fila': 54, 'id_pregunta': 1, 'id_situacion': 22},
        {'id_fila': 55, 'id_pregunta': 2, 'id_situacion': 22},
        {'id_fila': 56, 'id_pregunta': 7, 'id_situacion': 22},
        {'id_fila': 57, 'id_pregunta': 1, 'id_situacion': 23},
        {'id_fila': 58, 'id_pregunta': 2, 'id_situacion': 23},
        {'id_fila': 59, 'id_pregunta': 3, 'id_situacion': 23},
        {'id_fila': 60, 'id_pregunta': 4, 'id_situacion': 23},
        {'id_fila': 61, 'id_pregunta': 5, 'id_situacion': 23},
        
         ]
    for fila_data in filas:
        fila = Fila.query.get(fila_data['id_fila'])
        if not fila:
            new_fila = Fila(**fila_data)
            db.session.add(new_fila)

    db.session.commit()
    print('Filas creadas o ya existentes.')

# Llama a la función para crear las filas
crear_filas()
