from utils.ma import ma
from marshmallow import fields
from model.pregunta import Pregunta 

class PreguntaSchema(ma.Schema):
    class Meta:
        model = Pregunta
        fields = (
            'id_pregunta',
            'enunciado'
        )

pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many=True)
