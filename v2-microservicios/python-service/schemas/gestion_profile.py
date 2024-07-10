from utils.ma import ma
from model.especialista import Especialista
from model.persona import Persona
from model.usuario import Usuario
from model.ubicacion import Ubicacion
from model.paciente import Paciente
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = (
            'email',
        )

class UbicacionSchema(ma.Schema):
    class Meta:
        model = Ubicacion
        fields = (
            'provincia',
            'distrito',
        )

class PersonaSchema(ma.Schema):
    usuario = fields.Nested(UsuarioSchema)
    ubicacion = fields.Nested(UbicacionSchema)

    class Meta:
        model = Persona
        fields = (
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'sexo',
            'estado_civil',
            'celular',
            'usuario',
            'ubicacion',
        )

class EspecialistaProfileSchema(ma.Schema):
    persona = fields.Nested(PersonaSchema)

    class Meta:
        model = Especialista
        fields = (
            'especialidad',
            'experiencia',
            'persona',
        )

especialista_profile_schema = EspecialistaProfileSchema()

class PacienteProfileSchema(ma.Schema):
    class Meta:
        model = Paciente
        fields = (
            'antecedentes',
            'persona',
        )
    
    persona = fields.Nested(PersonaSchema)

paciente_profile_schema = PacienteProfileSchema()
