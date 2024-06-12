from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id_pregunta = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(255))

def __init__(self, id_pregunta, enunciado):
        self.id_pregunta = id_pregunta
        self.enunciado = enunciado

def crear_preguntas():
    preguntas = [
        {'id_pregunta': 1, 'enunciado': 'Me preocupo fácilmente.'},
        {'id_pregunta': 2, 'enunciado': 'Tengo pensamientos o sentimientos negativos sobre mí, tales como "inferior a los demás, torpe, etc."'},
        {'id_pregunta': 3, 'enunciado': 'Me siento inseguro de mí mismo.'},
        {'id_pregunta': 4, 'enunciado': 'Doy demasiadas vueltas a las cosas sin llegar a decidirme.'},
        {'id_pregunta': 5, 'enunciado': 'Siento miedo.'},
        {'id_pregunta': 6, 'enunciado': 'Me cuesta concentrarme.'},
        {'id_pregunta': 7, 'enunciado': 'Pienso que la gente se dará cuenta de mis problemas o de la torpeza de mis actos.'},
        {'id_pregunta': 8, 'enunciado': 'Siento molestias en el estómago.'},
        {'id_pregunta': 9, 'enunciado': 'Me sudan las manos u otra parte del cuerpo hasta en días fríos.'},
        {'id_pregunta': 10, 'enunciado': 'Me tiemblan las manos o las piernas.'},
        {'id_pregunta': 11, 'enunciado': 'Me duele la cabeza.'},
        {'id_pregunta': 12, 'enunciado': 'Mi cuerpo está en tensión.'},
        {'id_pregunta': 13, 'enunciado': 'Tengo palpitaciones, el corazón me late muy deprisa.'},
        {'id_pregunta': 14, 'enunciado': 'Me falta el aire y mi respiración es agitada.'},
        {'id_pregunta': 15, 'enunciado': 'Siento náuseas o mareo.'},
        {'id_pregunta': 16, 'enunciado': 'Se me seca la boca y tengo dificultades para tragar.'},
        {'id_pregunta': 17, 'enunciado': 'Tengo escalofríos y tiritos aunque no haga mucho frío.'},
        {'id_pregunta': 18, 'enunciado': 'Lloro con facilidad.'},
        {'id_pregunta': 19, 'enunciado': 'Realizo movimientos repetitivos con alguna parte de mi cuerpo (rascarme, tocarme, movimientos rítmicos con pies o manos, etc.).'},
        {'id_pregunta': 20, 'enunciado': 'Fumo, como o bebo demasiado.'},
        {'id_pregunta': 21, 'enunciado': 'Trato de evitar o rehuir la situación.'},
        {'id_pregunta': 22, 'enunciado': 'Me muevo y hago cosas sin una finalidad concreta.'},
        {'id_pregunta': 23, 'enunciado': 'Quedo paralizado o mis movimientos son torpes.'},
        {'id_pregunta': 24, 'enunciado': 'Tartamudeo o tengo otras dificultades de expresión verbal.'}
    ]

    for pregunta_data in preguntas:
        pregunta = Pregunta.query.get(pregunta_data['id_pregunta'])
        if not pregunta:
            new_pregunta = Pregunta(**pregunta_data)
            db.session.add(new_pregunta)

    db.session.commit()
    print('Preguntas creadas o ya existentes.')
