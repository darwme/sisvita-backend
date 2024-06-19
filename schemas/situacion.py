from utils.ma import ma
from model.situacion import Situacion
from marshmallow import fields
from schemas.seccion import SeccionSchema

class SituacionSchema(ma.Schema):
    class Meta:
        model = Situacion
        fields = (
            'id_situacion',
            'seccion',
            'descripcion',
            'cant_preguntas',
        )
    seccion = fields.Nested(SeccionSchema)

situacion_schema = SituacionSchema()
situaciones_schema = SituacionSchema(many=True)