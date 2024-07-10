from utils.ma import ma
from model.ubicacion import Ubicacion

class UbicacionSchema(ma.Schema):
    class Meta:
        model = Ubicacion
        fields = (
            'ubigeo',
            'distrito',
            'provincia',
            'y',
            'x',
        )

ubicacion_schema = UbicacionSchema()
ubicaciones_schema = UbicacionSchema(many=True)