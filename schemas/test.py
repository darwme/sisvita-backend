from utils.ma import ma
from model.test import Test
from marshmallow import fields

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
            'id_test',
            'nombre',
            'descripcion',
        )

test_schema = TestSchema()
tests_schema = TestSchema(many=True)