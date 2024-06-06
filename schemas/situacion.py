from utils.ma import ma
from marshmallow import fields
from model.situacion import Situacion

class SituacionSchema(ma.Schema):
    class Meta:
        model = Situacion
        fields = (
            'id_situacion',
            'seccion',
            'enunciado'
        )

situacion_schema = SituacionSchema()
situaciones_schema = SituacionSchema(many=True)
