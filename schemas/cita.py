from utils.ma import ma
from model.cita import Cita  
from marshmallow import fields

class CitaSchema(ma.Schema):
    class Meta:
        model = Cita
        fields = (
            'id_cita',
            'id_especialista', 
            'id_paciente',  
            'fecha_agenda',
            'estado',
            'motivo'
        )
cita_schema = CitaSchema()
citas_schema = CitaSchema(many=True)
