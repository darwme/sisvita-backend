# schemas/historial_test.py
from utils.ma import ma
from model.historial_test import Historial_test
from model.seccion import Seccion
from schemas.test import TestSchema
from marshmallow import fields

class Historial_testSchema(ma.Schema):
    class Meta:
        model = Historial_test
        fields = (
            #'id_usuario',
            'fecha_realizada',
            'puntajes',
            'diagnosticos',
            'test',
            'secciones'
        )

    test = fields.Method("get_test_nombre")
    secciones = fields.Method("get_secciones")

    def get_test_nombre(self, obj):
        return obj.test.nombre

    def get_secciones(self, obj):
        secciones = Seccion.query.filter_by(id_test=obj.id_test).all()
        return ','.join([seccion.descripcion for seccion in secciones])

historial_test_schema = Historial_testSchema()
historiales_tests_schema = Historial_testSchema(many=True)
