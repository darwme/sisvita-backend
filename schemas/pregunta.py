from utils.ma import ma
from model.pregunta import Pregunta
from marshmallow import fields
from schemas.situacion import SituacionSchema

class PreguntaSchema(ma.Schema):
    class Meta:
        model = Pregunta
        fields = (
            'id_pregunta',
            #'situacion',
            'descripcion',
        )
    situacion = fields.Nested(SituacionSchema)

pregunta_schema = SituacionSchema()
preguntas_schema = SituacionSchema(many=True)