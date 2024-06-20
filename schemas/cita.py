from utils.ma import ma
from model.cita import Cita  
from marshmallow import fields
from schemas.especialista import EspecialistaSchema
from schemas.paciente import PacienteSchema

class CitaSchema(ma.Schema):
    class Meta:
        model = Cita
        fields = (
            'id_cita',
            'especialista', 
            'paciente',  
            'fecha_agenda',
            'estado',
            'motivo',
            'hora',
        )
    especialista = fields.Nested(EspecialistaSchema)
    paciente = fields.Nested(PacienteSchema)

cita_schema = CitaSchema()
citas_schema = CitaSchema(many=True)
