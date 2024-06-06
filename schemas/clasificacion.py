from utils.ma import ma
from marshmallow import fields
from model.clasificacion import Clasificacion

class ClasificacionSchema(ma.Schema):
    class Meta:
        model = Clasificacion
        fields = (
            'id_clasificacion',
            'nombre',
            'categoria',
            'minimo',
            'maximo',
            'sexo'
        )

clasificacion_schema = ClasificacionSchema()
clasificaciones_schema = ClasificacionSchema(many=True)
