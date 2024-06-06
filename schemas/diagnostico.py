from utils.ma import ma
from marshmallow import fields
from model.diagnostico import Diagnostico

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = (
            'id_diagnostico',
            'id_test',
            'id_clasificacion',
            'categoria',
            'puntaje'
        )

diagnostico_schema = DiagnosticoSchema()
diagnosticos_schema = DiagnosticoSchema(many=True)
