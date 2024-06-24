from utils.ma import ma
from model.seccion_respuesta import Seccion_respuesta
from marshmallow import fields
from schemas.usuario import UsuarioSchema
from schemas.test import TestSchema
from schemas.seccion import SeccionSchema

class Seccion_respuestaSchema(ma.Schema):
    class Meta:
        model = Seccion_respuesta
        fields = (
            'id_seccion_respuesta',
            'usuario',
            'test',
            'seccion',
            'respuestas'
        )
    usuario = fields.Nested(UsuarioSchema)
    test = fields.Nested(TestSchema)
    seccion = fields.Nested(SeccionSchema)

seccion_respuesta_schema = Seccion_respuestaSchema()
seccion_respuestas_schema = Seccion_respuestaSchema(many=True)