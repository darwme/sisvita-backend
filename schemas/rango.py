from utils.ma import ma
from model.rango import Rango
from marshmallow import fields
from schemas.test import TestSchema

class RangoSchema(ma.Schema):
    class Meta:
        model = Rango
        fields = (
            'id_rango',
            'test',
            'minimo',
            'maximo',
            'diagnostico',
        )
    test = fields.Nested(TestSchema)

rango_schema = RangoSchema()
rangos_schema = RangoSchema(many=True)