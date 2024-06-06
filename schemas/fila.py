from utils.ma import ma
from marshmallow import fields
from model.fila import Fila

class FilaSchema(ma.Schema):
    class Meta:
        model = Fila
        fields = (
            'id_fila',
            'id_pregunta',
            'id_situacion'
        )

fila_schema = FilaSchema()
filas_schema = FilaSchema(many=True)
