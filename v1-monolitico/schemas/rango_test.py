from utils.ma import ma
from model.rango_test import Rango_test
from marshmallow import fields
from schemas.test import TestSchema

class Rango_testSchema(ma.Schema):
    class Meta:
        model = Rango_test
        fields = (
            'id_rango_test',
            'id_test',
            'minimo',
            'maximo',
            'diagnostico',
        )

    id_test = fields.Method("get_id_test")
    secciones = fields.Method("get_secciones")

    def get_id_test(self, obj):
        return obj.test.id_test

rango_test_schema = Rango_testSchema()
rango_tests_schema = Rango_testSchema(many=True)