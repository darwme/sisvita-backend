from utils.db import db
from dataclasses import dataclass

@dataclass
class Fila(db.Model):
    __tablename__ = 'fila'
    id_fila = db.Column(db.Integer, primary_key=True)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'), nullable=False)
    id_situacion = db.Column(db.Integer, db.ForeignKey('situacion.id_situacion'), nullable=False)

    pregunta = db.relationship('Pregunta', backref='filas')
    situacion = db.relationship('Situacion', backref='filas')
    
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
        {'id_fila': 57, 'id_pregunta': 3, 'id_situacion': 1},
        {'id_fila': 58, 'id_pregunta': 4, 'id_situacion': 1},
        {'id_fila': 59, 'id_pregunta': 5, 'id_situacion': 1},
        {'id_fila': 60, 'id_pregunta': 7, 'id_situacion': 1},
        {'id_fila': 61, 'id_pregunta': 8, 'id_situacion': 1},
        {'id_fila': 62, 'id_pregunta': 9, 'id_situacion': 1},
        {'id_fila': 63, 'id_pregunta': 10, 'id_situacion': 1},
        {'id_fila': 64, 'id_pregunta': 1, 'id_situacion': 2},
        {'id_fila': 65, 'id_pregunta': 2, 'id_situacion': 2},
        {'id_fila': 66, 'id_pregunta': 3, 'id_situacion': 2},
        {'id_fila': 67, 'id_pregunta': 4, 'id_situacion': 2},
        {'id_fila': 68, 'id_pregunta': 6, 'id_situacion': 2},
        {'id_fila': 69, 'id_pregunta': 7, 'id_situacion': 2},
        {'id_fila': 70, 'id_pregunta': 9, 'id_situacion': 2},
        {'id_fila': 71, 'id_pregunta': 1, 'id_situacion': 3},
        {'id_fila': 72, 'id_pregunta': 2, 'id_situacion': 3},
        {'id_fila': 73, 'id_pregunta': 3, 'id_situacion': 3},
        {'id_fila': 74, 'id_pregunta': 4, 'id_situacion': 3},
        {'id_fila': 75, 'id_pregunta': 6, 'id_situacion': 3},
        {'id_fila': 76, 'id_pregunta': 7, 'id_situacion': 3},
        {'id_fila': 77, 'id_pregunta': 8, 'id_situacion': 3},
        {'id_fila': 78, 'id_pregunta': 9, 'id_situacion': 3},
        {'id_fila': 79, 'id_pregunta': 4, 'id_situacion': 4},
        {'id_fila': 80, 'id_pregunta': 1, 'id_situacion': 5},
        {'id_fila': 81, 'id_pregunta': 4, 'id_situacion': 5},
        {'id_fila': 82, 'id_pregunta': 6, 'id_situacion': 5},
        {'id_fila': 83, 'id_pregunta': 9, 'id_situacion': 5},
        {'id_fila': 84, 'id_pregunta': 1, 'id_situacion': 6},
        {'id_fila': 85, 'id_pregunta': 5, 'id_situacion': 6},
        {'id_fila': 86, 'id_pregunta': 7, 'id_situacion': 6},
        {'id_fila': 87, 'id_pregunta': 9, 'id_situacion': 6},
        {'id_fila': 88, 'id_pregunta': 3, 'id_situacion': 7},
        {'id_fila': 89, 'id_pregunta': 6, 'id_situacion': 7},
        {'id_fila': 90, 'id_pregunta': 7, 'id_situacion': 7},
        {'id_fila': 91, 'id_pregunta': 8, 'id_situacion': 7},
        {'id_fila': 92, 'id_pregunta': 9, 'id_situacion': 7},
        {'id_fila': 93, 'id_pregunta': 1, 'id_situacion': 8},
        {'id_fila': 94, 'id_pregunta': 3, 'id_situacion': 8},
        {'id_fila': 95, 'id_pregunta': 4, 'id_situacion': 8},
        {'id_fila': 96, 'id_pregunta': 6, 'id_situacion': 8},
        {'id_fila': 97, 'id_pregunta': 7, 'id_situacion': 8},
        {'id_fila': 98, 'id_pregunta': 8, 'id_situacion': 8},
        {'id_fila': 99, 'id_pregunta': 9, 'id_situacion': 8},
        {'id_fila': 100, 'id_pregunta': 3, 'id_situacion': 9},
        {'id_fila': 101, 'id_pregunta': 7, 'id_situacion': 9},
        {'id_fila': 102, 'id_pregunta': 8, 'id_situacion': 9},
        {'id_fila': 103, 'id_pregunta': 9, 'id_situacion': 9},
        {'id_fila': 104, 'id_pregunta': 1, 'id_situacion': 10},
        {'id_fila': 105, 'id_pregunta': 3, 'id_situacion': 10},
        {'id_fila': 106, 'id_pregunta': 4, 'id_situacion': 10},
        {'id_fila': 107, 'id_pregunta': 6, 'id_situacion': 10},
        {'id_fila': 108, 'id_pregunta': 7, 'id_situacion': 10},
        {'id_fila': 109, 'id_pregunta': 8, 'id_situacion': 10},
        {'id_fila': 110, 'id_pregunta': 9, 'id_situacion': 10},
        {'id_fila': 111, 'id_pregunta': 10, 'id_situacion': 10},
        {'id_fila': 112, 'id_pregunta': 5, 'id_situacion': 11},
        {'id_fila': 113, 'id_pregunta': 6, 'id_situacion': 11},
        {'id_fila': 114, 'id_pregunta': 7, 'id_situacion': 11},
        {'id_fila': 115, 'id_pregunta': 10, 'id_situacion': 11},
        {'id_fila': 116, 'id_pregunta': 2, 'id_situacion': 12},
        {'id_fila': 117, 'id_pregunta': 3, 'id_situacion': 12},
        {'id_fila': 118, 'id_pregunta': 4, 'id_situacion': 12},
        {'id_fila': 119, 'id_pregunta': 6, 'id_situacion': 12},
        {'id_fila': 120, 'id_pregunta': 7, 'id_situacion': 12},
        {'id_fila': 121, 'id_pregunta': 8, 'id_situacion': 12},
        {'id_fila': 122, 'id_pregunta': 9, 'id_situacion': 12},
        {'id_fila': 123, 'id_pregunta': 2, 'id_situacion': 13},
        {'id_fila': 124, 'id_pregunta': 3, 'id_situacion': 13},
        {'id_fila': 125, 'id_pregunta': 4, 'id_situacion': 13},
        {'id_fila': 126, 'id_pregunta': 7, 'id_situacion': 13},
        {'id_fila': 127, 'id_pregunta': 10, 'id_situacion': 13},
        {'id_fila': 128, 'id_pregunta': 4, 'id_situacion': 14},
        {'id_fila': 129, 'id_pregunta': 7, 'id_situacion': 14},
        {'id_fila': 130, 'id_pregunta': 10, 'id_situacion': 14},
        {'id_fila': 131, 'id_pregunta': 3, 'id_situacion': 15},
        {'id_fila': 132, 'id_pregunta': 4, 'id_situacion': 15},
        {'id_fila': 133, 'id_pregunta': 7, 'id_situacion': 15},
        {'id_fila': 134, 'id_pregunta': 9, 'id_situacion': 15},
        {'id_fila': 135, 'id_pregunta': 2, 'id_situacion': 16},
        {'id_fila': 136, 'id_pregunta': 3, 'id_situacion': 16},
        {'id_fila': 137, 'id_pregunta': 4, 'id_situacion': 16},
        {'id_fila': 138, 'id_pregunta': 5, 'id_situacion': 16},
        {'id_fila': 139, 'id_pregunta': 7, 'id_situacion': 16},
        {'id_fila': 140, 'id_pregunta': 9, 'id_situacion': 16},
        {'id_fila': 141, 'id_pregunta': 1, 'id_situacion': 17},
        {'id_fila': 142, 'id_pregunta': 2, 'id_situacion': 17},
        {'id_fila': 143, 'id_pregunta': 3, 'id_situacion': 17},
        {'id_fila': 144, 'id_pregunta': 4, 'id_situacion': 17},
        {'id_fila': 145, 'id_pregunta': 7, 'id_situacion': 17},
        {'id_fila': 146, 'id_pregunta': 1, 'id_situacion': 18},
        {'id_fila': 147, 'id_pregunta': 3, 'id_situacion': 18},
        {'id_fila': 148, 'id_pregunta': 4, 'id_situacion': 18},
        {'id_fila': 149, 'id_pregunta': 7, 'id_situacion': 18},
        {'id_fila': 150, 'id_pregunta': 9, 'id_situacion': 18},
        {'id_fila': 151, 'id_pregunta': 3, 'id_situacion': 19},
        {'id_fila': 152, 'id_pregunta': 6, 'id_situacion': 19},
        {'id_fila': 153, 'id_pregunta': 7, 'id_situacion': 19},
        {'id_fila': 154, 'id_pregunta': 8, 'id_situacion': 19},
        {'id_fila': 155, 'id_pregunta': 9, 'id_situacion': 19},
        {'id_fila': 156, 'id_pregunta': 10, 'id_situacion': 19},
        {'id_fila': 157, 'id_pregunta': 1, 'id_situacion': 20},
        {'id_fila': 158, 'id_pregunta': 6, 'id_situacion': 20},
        {'id_fila': 159, 'id_pregunta': 7, 'id_situacion': 20},
        {'id_fila': 160, 'id_pregunta': 8, 'id_situacion': 20},
        {'id_fila': 161, 'id_pregunta': 1, 'id_situacion': 21},
        {'id_fila': 162, 'id_pregunta': 3, 'id_situacion': 21},
        {'id_fila': 163, 'id_pregunta': 4, 'id_situacion': 21},
        {'id_fila': 164, 'id_pregunta': 6, 'id_situacion': 21},
        {'id_fila': 165, 'id_pregunta': 7, 'id_situacion': 21},
        {'id_fila': 166, 'id_pregunta': 8, 'id_situacion': 21},
        {'id_fila': 167, 'id_pregunta': 9, 'id_situacion': 21},
        {'id_fila': 168, 'id_pregunta': 4, 'id_situacion': 22},
        {'id_fila': 169, 'id_pregunta': 2, 'id_situacion': 1},
        {'id_fila': 170, 'id_pregunta': 5, 'id_situacion': 1},
        {'id_fila': 171, 'id_pregunta': 6, 'id_situacion': 1},
        {'id_fila': 172, 'id_pregunta': 2, 'id_situacion': 2},
        {'id_fila': 173, 'id_pregunta': 5, 'id_situacion': 2},
        {'id_fila': 174, 'id_pregunta': 1, 'id_situacion': 3},
        {'id_fila': 175, 'id_pregunta': 2, 'id_situacion': 3},
        {'id_fila': 176, 'id_pregunta': 3, 'id_situacion': 3},
        {'id_fila': 177, 'id_pregunta': 5, 'id_situacion': 3},
        {'id_fila': 178, 'id_pregunta': 6, 'id_situacion': 3},
        {'id_fila': 179, 'id_pregunta': 7, 'id_situacion': 3},
        {'id_fila': 180, 'id_pregunta': 3, 'id_situacion': 4},
        {'id_fila': 181, 'id_pregunta': 5, 'id_situacion': 4},
        {'id_fila': 182, 'id_pregunta': 7, 'id_situacion': 4},
        {'id_fila': 183, 'id_pregunta': 1, 'id_situacion': 5},
        {'id_fila': 184, 'id_pregunta': 3, 'id_situacion': 5},
        {'id_fila': 185, 'id_pregunta': 6, 'id_situacion': 5},
        {'id_fila': 186, 'id_pregunta': 3, 'id_situacion': 6},
        {'id_fila': 187, 'id_pregunta': 4, 'id_situacion': 6},
        {'id_fila': 188, 'id_pregunta': 3, 'id_situacion': 7},
        {'id_fila': 189, 'id_pregunta': 2, 'id_situacion': 8},
        {'id_fila': 190, 'id_pregunta': 3, 'id_situacion': 8},
        {'id_fila': 191, 'id_pregunta': 6, 'id_situacion': 8},
        {'id_fila': 192, 'id_pregunta': 2, 'id_situacion': 9},
        {'id_fila': 193, 'id_pregunta': 3, 'id_situacion': 9},
        {'id_fila': 194, 'id_pregunta': 6, 'id_situacion': 9},
        {'id_fila': 195, 'id_pregunta': 3, 'id_situacion': 10},
        {'id_fila': 196, 'id_pregunta': 2, 'id_situacion': 11},
        {'id_fila': 197, 'id_pregunta': 3, 'id_situacion': 11},
        {'id_fila': 198, 'id_pregunta': 5, 'id_situacion': 11},
        {'id_fila': 199, 'id_pregunta': 2, 'id_situacion': 12},
        {'id_fila': 200, 'id_pregunta': 4, 'id_situacion': 12},
        {'id_fila': 201, 'id_pregunta': 5, 'id_situacion': 12},
        {'id_fila': 202, 'id_pregunta': 6, 'id_situacion': 12},
        {'id_fila': 203, 'id_pregunta': 1, 'id_situacion': 13},
        {'id_fila': 204, 'id_pregunta': 3, 'id_situacion': 13},
        {'id_fila': 205, 'id_pregunta': 5, 'id_situacion': 14},
        {'id_fila': 206, 'id_pregunta': 7, 'id_situacion': 14},
        {'id_fila': 207, 'id_pregunta': 4, 'id_situacion': 15},
        {'id_fila': 208, 'id_pregunta': 2, 'id_situacion': 16},
        {'id_fila': 209, 'id_pregunta': 3, 'id_situacion': 16},
        {'id_fila': 210, 'id_pregunta': 1, 'id_situacion': 17},
        {'id_fila': 211, 'id_pregunta': 2, 'id_situacion': 17},
        {'id_fila': 212, 'id_pregunta': 3, 'id_situacion': 17},
        {'id_fila': 213, 'id_pregunta': 5, 'id_situacion': 17},
        {'id_fila': 214, 'id_pregunta': 6, 'id_situacion': 17},
        {'id_fila': 215, 'id_pregunta': 1, 'id_situacion': 18},
        {'id_fila': 216, 'id_pregunta': 3, 'id_situacion': 18},
        {'id_fila': 217, 'id_pregunta': 4, 'id_situacion': 18},
        {'id_fila': 218, 'id_pregunta': 6, 'id_situacion': 18},
        {'id_fila': 219, 'id_pregunta': 7, 'id_situacion': 18},
        {'id_fila': 220, 'id_pregunta': 6, 'id_situacion': 19},
        {'id_fila': 221, 'id_pregunta': 3, 'id_situacion': 20},
        {'id_fila': 222, 'id_pregunta': 5, 'id_situacion': 20},
        {'id_fila': 223, 'id_pregunta': 7, 'id_situacion': 21},
        {'id_fila': 224, 'id_pregunta': 5, 'id_situacion': 22},
         ]
    for fila_data in filas:
        fila = Fila.query.get(fila_data['id_fila'])
        if not fila:
            new_fila = Fila(**fila_data)
            db.session.add(new_fila)

    db.session.commit()
    print('Filas creadas o ya existentes.')


