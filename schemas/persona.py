from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    id_persona = fields.Integer()
    id_usuario = fields.Integer()
    nombre = fields.String()
    apellidos = fields.String()
    sexo = fields.String()
    estado_civil = fields.String()
    fecha_nacimiento = fields.Date()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
