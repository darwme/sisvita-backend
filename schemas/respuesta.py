from utils.ma import ma
from model.respuesta import Respuesta
from marshmallow import fields
from schemas.pregunta import PreguntaSchema

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuesta
        fields = (
            'id_respuesta',
            'pregunta',
            'valor',
        )
    pregunta = fields.Nested(PreguntaSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)