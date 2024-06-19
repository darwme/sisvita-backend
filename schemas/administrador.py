from utils.ma import ma
from model.administrador import Administrador  
from marshmallow import fields
from schemas.usuario import UsuarioSchema

class AdministradorSchema(ma.Schema):
    class Meta:
        model = Administrador
        fields = (
            'id_administrador',
            'id_usuario', 
            'nombre_admin'
        )

    usuario = fields.Nested(UsuarioSchema)
administrador_schema = AdministradorSchema()
administradores_schema = AdministradorSchema(many=True)
