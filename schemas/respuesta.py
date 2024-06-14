from utils.ma import ma
from model.respuesta import Respuesta
from marshmallow import fields
from schemas.test import TestSchema
from schemas.fila import FilaSchema

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuesta
        fields = (
            'id_respuesta',
            'id_fila',
            'id_test',
            'valor'
        )
    test = fields.Nested(TestSchema)
    fila = fields.Nested(FilaSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)

