from utils.ma import ma
from model.seccion import Seccion
from marshmallow import fields
from schemas.test import TestSchema

class SeccionSchema(ma.Schema):
    class Meta:
        model = Seccion
        fields = (
            'id_seccion',
            #'test',
            'descripcion',
        )
    test = fields.Nested(TestSchema)

seccion_schema = SeccionSchema()
secciones_schema = SeccionSchema(many=True)