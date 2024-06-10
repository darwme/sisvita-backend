from utils.ma import ma
from model.diagnostico import Diagnostico
from marshmallow import fields
from schemas.test import TestSchema
from schemas.clasificacion import ClasificacionSchema

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = (
            'id_diagnostico',
            'test',
            'categoria',
            'puntaje',
            'clasificacion'
        )
    test = fields.Nested(TestSchema)
    clasificacion = fields.Nested(ClasificacionSchema)

Diagnostico_schema = TestSchema()
Diagnosticos_schema = TestSchema(many=True)

