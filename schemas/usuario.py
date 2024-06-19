from utils.ma import ma
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = (
            'id_usuario',
            'clave',
            'email'
        )
usuario_schema = UsuarioSchema()
