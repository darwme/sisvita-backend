from utils.ma import ma
from model.test import Test
from marshmallow import fields
from schemas.estudiante import EstudianteSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
            'id_test',
            'clasificacion',
            'total_test',
            'fecha',
            'estudiante'
        )
    estudiante = fields.Nested(EstudianteSchema)

test_schema = TestSchema()
tests_schema = TestSchema(many=True)

