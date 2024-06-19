from utils.ma import ma
from model.historial_respuesta import Historial_respuesta
from marshmallow import fields
from schemas.historial_test import Historial_testSchema
from schemas.respuesta import RespuestaSchema

class Historial_respuestaSchema(ma.Schema):
    class Meta:
        model = Historial_respuesta
        fields = (
            'id_historial_test',
            'historial_test',
            'id_pregunta',
            'respuesta',
        )

    historial_test = fields.Nested(Historial_testSchema)
    respuesta = fields.Nested(RespuestaSchema)

Historial_respuesta_schema = Historial_respuestaSchema()
Historiales_respuestas_schema = Historial_respuestaSchema(many=True)
