from utils.ma import ma
from marshmallow import fields
from model.seccion import Seccion

class SeccionSchema(ma.Schema):
    class Meta:
        model = Seccion
        fields = (
            'id_seccion',
            'nombre'
        )

seccion_schema = SeccionSchema()
secciones_schema = SeccionSchema(many=True)
