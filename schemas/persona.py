from utils.ma import ma
from model.persona import Persona
from marshmallow import fields
from schemas.usuario import UsuarioSchema

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'id_persona',
            'usuario', 
            'nombres',
            'apellidos',
            'sexo',
            'estado_civil',
            'fecha_nacimiento',
            'celular',
        )
    usuario = fields.Nested(UsuarioSchema)


persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
