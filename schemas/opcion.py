from utils.ma import ma
from model.opcion import Opcion
from marshmallow import fields
from schemas.test import TestSchema

class OpcionSchema(ma.Schema):
    class Meta:
        model = Opcion
        fields = (
            #'id_opcion',
            #'test',
            'descripcion',
            'valor_opcion',
        )
    #test = fields.Nested(TestSchema)

opcion_schema = OpcionSchema()
opciones_schema = OpcionSchema(many=True)