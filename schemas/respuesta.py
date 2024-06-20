from utils.ma import ma
from model.respuesta import Respuesta
from marshmallow import fields
from schemas.pregunta import PreguntaSchema
from schemas.historial_test import Historial_testSchema

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuesta
        fields = (
            'id_respuesta',
            'historial_test',
            'pregunta',
            'valor',
        )
    pregunta = fields.Nested(PreguntaSchema)
    historial_test = fields.Nested(Historial_testSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)