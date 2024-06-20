from utils.ma import ma
from model.usuario import Usuario
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'email',
            'clave',
        )

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
