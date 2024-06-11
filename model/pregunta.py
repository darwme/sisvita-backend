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
    enunciados = [
        "Me preocupo fácilmente.",
        "Tengo pensamientos o sentimientos negativos sobre mí, tales como 'inferior a los demás, torpe, etc.'",
        "Me siento inseguro de mí mismo.",
        "Doy demasiadas vueltas a las cosas sin llegar a decidirme.",
        "Siento miedo.",
        "Me cuesta concentrarme.",
        "Pienso que la gente se dará cuenta de mis problemas o de la torpeza de mis actos.",
        "Siento molestias en el estómago.",
        "Me sudan las manos u otra parte del cuerpo hasta en días fríos.",
        "Me tiemblan las manos o las piernas.",
        "Me duele la cabeza.",
        "Mi cuerpo está en tensión.",
        "Tengo palpitaciones, el corazón me late muy deprisa.",
        "Me falta el aire y mi respiración es agitada.",
        "Siento náuseas o mareo.",
        "Se me seca la boca y tengo dificultades para tragar.",
        "Tengo escalofríos y tiritos aunque no haga mucho frío.",
        "Lloro con facilidad.",
        "Realizo movimientos repetitivos con alguna parte de mi cuerpo (rascarme, tocarme, movimientos rítmicos con pies o manos, etc.).",
        "Fumo, como o bebo demasiado.",
        "Trato de evitar o rehuir la situación.",
        "Me muevo y hago cosas sin una finalidad concreta.",
        "Quedo paralizado o mis movimientos son torpes.",
        "Tartamudeo o tengo otras dificultades de expresión verbal."
    ]

    for i in range(len(enunciados)):
        id_pregunta = i + 1
        enunciado = enunciados[i]
        pregunta = Pregunta.query.get(id_pregunta)
        if not pregunta:
            nueva_pregunta = Pregunta(id_pregunta, enunciado)
            db.session.add(nueva_pregunta)

    db.session.commit()
    print('Preguntas creadas o ya existentes.')
