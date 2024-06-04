from utils.ma import ma
from model.especialista import Especialista
from marshmallow import fields
from schemas.usuario import UsuarioSchema

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = (
            'id_especialista',
            'codigo_especialista',
            'especialidad',
            'id_usuario',
            'usuario'
        )

    usuario = fields.Nested(UsuarioSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)

