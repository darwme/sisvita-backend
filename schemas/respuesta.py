from utils.ma import ma
from marshmallow import fields
from model.respuesta import Respuesta

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuesta
        fields = (
            'id_respuesta',
            'id_cuestionario',
            'id_fila',
            'valor'
        )

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)
