from utils.ma import ma
from model.persona import Persona
from marshmallow import fields
from schemas.usuario import UsuarioSchema
from schemas.ubicacion import UbicacionSchema

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'id_persona',
            'ubicacion',
            'usuario', 
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'sexo',
            'estado_civil',
            'celular',
            'tipo_persona'
        )
    usuario = fields.Nested(UsuarioSchema)
    ubicacion = fields.Nested(UbicacionSchema)

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
