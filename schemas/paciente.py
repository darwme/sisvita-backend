from utils.ma import ma
from model.paciente import Paciente  
from marshmallow import fields
from schemas.usuario import UsuarioSchema  

class PacienteSchema(ma.Schema):
    class Meta:
        model = Paciente
        fields = (
            'id_paciente',
            'codigo_paciente',
            'enfermedad',
            'id_usuario',
            'usuario'
        )
    
    usuario = fields.Nested(UsuarioSchema)

paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)
