from utils.ma import ma
from model.rango_seccion import Rango_seccion
from marshmallow import fields
from schemas.seccion import SeccionSchema

class Rango_seccionSchema(ma.Schema):
    class Meta:
        model = Rango_seccion
        fields = (
            'id_rango_seccion',
            'seccion',
            'minimo',
            'maximo',
            'diagnostico',
        )
    seccion = fields.Nested(SeccionSchema)

rango_seccion_schema = Rango_seccionSchema()
rango_secciones_schema = Rango_seccionSchema(many=True)