from utils.db import db
from dataclasses import dataclass

@dataclass
class Situacion(db.Model):
    __tablename__ = 'situacion'
    id_situacion = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(255))
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'))

    def __init__(self, id_situacion, enunciado, id_seccion):
        self.id_situacion = id_situacion
        self.enunciado = enunciado
        self.id_seccion = id_seccion

def crear_situaciones():
    situaciones = [
        {'id_situacion': 1, 'enunciado': 'Ante un examen importante o una entrevista laboral crucial', 'id_seccion': 1},
        {'id_situacion': 2, 'enunciado': 'Cuando llego tarde a una cita', 'id_seccion': 1},
        {'id_situacion': 3, 'enunciado': 'Cuando pienso en la cantidad de tareas pendientes', 'id_seccion': 1},
        {'id_situacion': 4, 'enunciado': 'Al tomar decisiones difíciles o resolver problemas', 'id_seccion': 1},
        {'id_situacion': 5, 'enunciado': 'En el trabajo o cuando estoy estudiando', 'id_seccion': 1},
        {'id_situacion': 6, 'enunciado': 'Cuando tengo que enfrentar una situación de conflicto', 'id_seccion': 1},
        {'id_situacion': 7, 'enunciado': 'Cuando una persona del sexo opuesto está cerca o en una situación íntima', 'id_seccion': 1},
        {'id_situacion': 8, 'enunciado': 'Cuando alguien me molesta o durante una discusión', 'id_seccion': 1},
        {'id_situacion': 9, 'enunciado': 'Cuando soy observado en el trabajo o sometido a supervisión', 'id_seccion': 1},
        {'id_situacion': 10, 'enunciado': 'Cuando recibo críticas o pienso que puedo ser juzgado negativamente', 'id_seccion': 1},
        {'id_situacion': 11, 'enunciado': 'Al hablar en público', 'id_seccion': 1},
        {'id_situacion': 12, 'enunciado': 'Cuando pienso en experiencias recientes que me causaron angustia', 'id_seccion': 1},
        {'id_situacion': 13, 'enunciado': 'Después de cometer un error', 'id_seccion': 1},
        {'id_situacion': 14, 'enunciado': 'Ante la consulta del dentista, inyecciones, heridas o sangre', 'id_seccion': 1},
        {'id_situacion': 15, 'enunciado': 'Antes de una cita con una persona del sexo opuesto', 'id_seccion': 1},
        {'id_situacion': 16, 'enunciado': 'Cuando pienso en mi futuro o en dificultades futuras', 'id_seccion': 1},
        {'id_situacion': 17, 'enunciado': 'En medio de multitudes o en espacios cerrados', 'id_seccion': 1},
        {'id_situacion': 18, 'enunciado': 'Cuando tengo que asistir a reuniones sociales o conocer gente nueva', 'id_seccion': 1},
        {'id_situacion': 19, 'enunciado': 'En lugares altos o frente a aguas profundas', 'id_seccion': 1},
        {'id_situacion': 20, 'enunciado': 'Al observar escenas violentas', 'id_seccion': 1},
        {'id_situacion': 21, 'enunciado': 'Sin razón específica', 'id_seccion': 1},
        {'id_situacion': 22, 'enunciado': 'A la hora de dormir', 'id_seccion': 1},
        {'id_situacion': 23, 'enunciado': 'Ante un examen importante o una entrevista laboral crucial', 'id_seccion': 2},
        {'id_situacion': 24, 'enunciado': 'Cuando llego tarde a una cita', 'id_seccion': 2},
        {'id_situacion': 25, 'enunciado': 'Cuando pienso en la cantidad de tareas pendientes', 'id_seccion': 2},
        {'id_situacion': 26, 'enunciado': 'Al tomar decisiones difíciles o resolver problemas', 'id_seccion': 2},
        {'id_situacion': 27, 'enunciado': 'En el trabajo o cuando estoy estudiando', 'id_seccion': 2},
        {'id_situacion': 28, 'enunciado': 'Cuando tengo que enfrentar una situación de conflicto', 'id_seccion': 2},
        {'id_situacion': 29, 'enunciado': 'Cuando una persona del sexo opuesto está cerca o en una situación íntima', 'id_seccion': 2},
        {'id_situacion': 30, 'enunciado': 'Cuando alguien me molesta o durante una discusión', 'id_seccion': 2},
        {'id_situacion': 31, 'enunciado': 'Cuando soy observado en el trabajo o sometido a supervisión', 'id_seccion': 2},
        {'id_situacion': 32, 'enunciado': 'Cuando recibo críticas o pienso que puedo ser juzgado negativamente', 'id_seccion': 2},
        {'id_situacion': 33, 'enunciado': 'Al hablar en público', 'id_seccion': 2},
        {'id_situacion': 34, 'enunciado': 'Cuando pienso en experiencias recientes que me causaron angustia', 'id_seccion': 2},
        {'id_situacion': 35, 'enunciado': 'Después de cometer un error', 'id_seccion': 2},
        {'id_situacion': 36, 'enunciado': 'Ante la consulta del dentista, inyecciones, heridas o sangre', 'id_seccion': 2},
        {'id_situacion': 37, 'enunciado': 'Antes de una cita con una persona del sexo opuesto', 'id_seccion': 2},
        {'id_situacion': 38, 'enunciado': 'Cuando pienso en mi futuro o en dificultades futuras', 'id_seccion': 2},
        {'id_situacion': 39, 'enunciado': 'En medio de multitudes o en espacios cerrados', 'id_seccion': 2},
        {'id_situacion': 40, 'enunciado': 'Cuando tengo que asistir a reuniones sociales o conocer gente nueva', 'id_seccion': 2},
        {'id_situacion': 41, 'enunciado': 'En lugares altos o frente a aguas profundas', 'id_seccion': 2},
        {'id_situacion': 42, 'enunciado': 'Al observar escenas violentas', 'id_seccion': 2},
        {'id_situacion': 43, 'enunciado': 'Sin razón específica', 'id_seccion': 2},
        {'id_situacion': 44, 'enunciado': 'A la hora de dormir', 'id_seccion': 2},
        {'id_situacion': 45, 'enunciado': 'Ante un examen importante o una entrevista laboral crucial', 'id_seccion': 3},
        {'id_situacion': 46, 'enunciado': 'Cuando llego tarde a una cita', 'id_seccion': 3},
        {'id_situacion': 47, 'enunciado': 'Cuando pienso en la cantidad de tareas pendientes', 'id_seccion': 3},
        {'id_situacion': 48, 'enunciado': 'Al tomar decisiones difíciles o resolver problemas', 'id_seccion': 3},
        {'id_situacion': 49, 'enunciado': 'En el trabajo o cuando estoy estudiando', 'id_seccion': 3},
        {'id_situacion': 50, 'enunciado': 'Cuando tengo que enfrentar una situación de conflicto', 'id_seccion': 3},
        {'id_situacion': 51, 'enunciado': 'Cuando una persona del sexo opuesto está cerca o en una situación íntima', 'id_seccion': 3},
        {'id_situacion': 52, 'enunciado': 'Cuando alguien me molesta o durante una discusión', 'id_seccion': 3},
        {'id_situacion': 53, 'enunciado': 'Cuando soy observado en el trabajo o sometido a supervisión', 'id_seccion': 3},
        {'id_situacion': 54, 'enunciado': 'Cuando recibo críticas o pienso que puedo ser juzgado negativamente', 'id_seccion': 3},
        {'id_situacion': 55, 'enunciado': 'Al hablar en público', 'id_seccion': 3},
        {'id_situacion': 56, 'enunciado': 'Cuando pienso en experiencias recientes que me causaron angustia', 'id_seccion': 3},
        {'id_situacion': 57, 'enunciado': 'Después de cometer un error', 'id_seccion': 3},
        {'id_situacion': 58, 'enunciado': 'Ante la consulta del dentista, inyecciones, heridas o sangre', 'id_seccion': 3},
        {'id_situacion': 59, 'enunciado': 'Antes de una cita con una persona del sexo opuesto', 'id_seccion': 3},
        {'id_situacion': 60, 'enunciado': 'Cuando pienso en mi futuro o en dificultades futuras', 'id_seccion': 3},
        {'id_situacion': 61, 'enunciado': 'En medio de multitudes o en espacios cerrados', 'id_seccion': 3},
        {'id_situacion': 62, 'enunciado': 'Cuando tengo que asistir a reuniones sociales o conocer gente nueva', 'id_seccion': 3},
        {'id_situacion': 63, 'enunciado': 'En lugares altos o frente a aguas profundas', 'id_seccion': 3},
        {'id_situacion': 64, 'enunciado': 'Al observar escenas violentas', 'id_seccion': 3},
        {'id_situacion': 65, 'enunciado': 'Sin razón específica', 'id_seccion': 3},
        {'id_situacion': 66, 'enunciado': 'A la hora de dormir', 'id_seccion': 3},
    ]

    for situacion_data in situaciones:
        situacion = Situacion.query.get(situacion_data['id_situacion'])
        if not situacion:
            new_situacion = Situacion(**situacion_data)
            db.session.add(new_situacion)

    db.session.commit()
    print('Situaciones creadas o ya existentes.')
