from utils.ma import ma
from marshmallow import fields
from model.evaluacion import Evaluacion
from model.historial_test import Historial_test
from model.especialista import Especialista
from model.paciente import Paciente
from model.persona import Persona
from model.test import Test 
from schemas.usuario import UsuarioSchema 

class PersonaSchema(ma.Schema):
    usuario = fields.Nested(UsuarioSchema)

    class Meta:
        model = Persona
        fields = (
            'nombres',
            'apellidos',
        )

class EspecialistaProfileSchema(ma.Schema):
    persona = fields.Nested(PersonaSchema)

    class Meta:
        model = Especialista
        fields = (
            'persona',
            'especialidad',
        )

class PacienteProfileSchema(ma.Schema):
    persona = fields.Nested(PersonaSchema)

    class Meta:
        model = Paciente
        fields = (
            'persona',
        )

class HistorialTestSchema(ma.Schema):
    class Meta:
        model = Historial_test
        fields = (
            'fecha_realizada',
            'diagnosticos',
            'test_nombre',
        )

    # Campo derivado del test
    test_nombre = fields.Method("get_test_nombre")

    def get_test_nombre(self, obj):
        return obj.test.nombre

class EvaluacionSchema(ma.Schema):
    especialista = fields.Nested(EspecialistaProfileSchema)
    paciente = fields.Nested(PacienteProfileSchema)
    historial_test = fields.Nested(HistorialTestSchema)

    class Meta:
        model = Evaluacion
        fields = (
            'id_evaluacion',
            'especialista',
            'paciente',
            'historial_test',
            'fecha_evaluacion',
            'fundamento_cientifico',  
            'tratamiento',
            'descripcion_tratamiento',
            'comunicacion'
        )

# Creación de instancias de los esquemas
evaluacion_schema = EvaluacionSchema()
evaluaciones_schema = EvaluacionSchema(many=True)
