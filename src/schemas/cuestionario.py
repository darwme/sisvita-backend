from utils.ma import ma
from model.cuestionario import Cuestionario
from marshmallow import fields
from schemas.seccion import SeccionSchema
from schemas.test import TestSchema

class CuestionarioSchema(ma.Schema):
    class Meta:
        model = Cuestionario
        fields = (
            'id_cuestionario',
            'total_cuestionario'
        )
    seccion = fields.Nested(SeccionSchema)
    test = fields.Nested(TestSchema)

cuestionario_schema = CuestionarioSchema()
cuestionarios_schema = CuestionarioSchema(many=True)
