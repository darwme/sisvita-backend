from utils.ma import ma
from model.historial_test import Historial_test
from marshmallow import fields
from schemas.usuario import UsuarioSchema
from schemas.test import TestSchema

class Historial_testSchema(ma.Schema):
    class Meta:
        model = Historial_test
        fields = (
            'id_historial_test',
            'usuario',
            'test',
            'fecha_realizada',
            'cant_preguntas_realizadas',
            'puntaje_realizado',
            'array_diagnostico',
        )
    usuario = fields.Nested(UsuarioSchema)
    test = fields.Nested(TestSchema)

historial_test_schema = Historial_testSchema()
historiales_tests_schema = Historial_testSchema(many=True)