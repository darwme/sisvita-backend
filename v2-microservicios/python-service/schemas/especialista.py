from utils.ma import ma
from model.especialista import Especialista  
from marshmallow import fields
from schemas.persona import PersonaSchema

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = (
            'id_especialista',
            'persona', 
            'codigo_especialista',
            'especialidad',
            'experiencia',        )

    persona = fields.Nested(PersonaSchema)
    
especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)
