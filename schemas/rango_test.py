from utils.ma import ma
from model.rango_test import Rango_test
from marshmallow import fields
from schemas.test import TestSchema

class Rango_testSchema(ma.Schema):
    class Meta:
        model = Rango_test
        fields = (
            'id_rango_test',
            'test',
            'minimo',
            'maximo',
            'diagnostico',
        )
    test = fields.Nested(TestSchema)

rango_test_schema = Rango_testSchema()
rango_tests_schema = Rango_testSchema(many=True)