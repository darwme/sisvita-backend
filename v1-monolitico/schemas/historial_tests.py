from utils.ma import ma
from model.historial_test import Historial_test
from model.seccion import Seccion
from schemas.test import TestSchema
from marshmallow import fields
from model.usuario import Usuario
from model.persona import Persona
from model.paciente import Paciente
from model.ubicacion import Ubicacion
from model.rango_test import Rango_test

class Historial_test_e_Schema(ma.Schema):
    class Meta:
        model = Historial_test
        fields = (
            'codigo_historial_test',
            'paciente',  # Agregada coma aquí
            'fecha_realizada',
            'puntajes',
            'diagnosticos',
            'test',
            'secciones',
            'estado',
            'ubicacion',
            'codigo_paciente',
        )

    test = fields.Method("get_test_nombre")
    secciones = fields.Method("get_secciones")
    paciente = fields.Method("get_nombre_paciente")
    ubicacion = fields.Method("get_ubicacion")
    codigo_paciente = fields.Method("get_codigo_paciente")

    def get_test_nombre(self, obj):
        return obj.test.nombre if obj.test else None

    def get_secciones(self, obj):
        secciones = Seccion.query.filter_by(id_test=obj.id_test).all()
        return ','.join([seccion.descripcion for seccion in secciones])

    def get_nombre_paciente(self, obj):
        usuario = Usuario.query.get(obj.id_usuario)
        if usuario:
            persona = Persona.query.filter_by(id_usuario=usuario.id_usuario).first()
            if persona:
                paciente = Paciente.query.filter_by(id_persona=persona.id_persona).first()
                if paciente:
                    return f"{persona.nombres} {persona.apellidos} "  # Ajusta según la estructura real de tu base de datos
        return None
    
    def get_codigo_paciente(self, obj):
        usuario = Usuario.query.get(obj.id_usuario)
        if usuario:
            persona = Persona.query.filter_by(id_usuario=usuario.id_usuario).first()
            if persona:
                paciente = Paciente.query.filter_by(id_persona=persona.id_persona).first()
                if paciente:
                    return paciente.codigo_paciente
        return None
    
    
    def get_ubicacion(self, obj):
        usuario = Usuario.query.get(obj.id_usuario)
        if usuario:
            persona = Persona.query.filter_by(id_usuario=usuario.id_usuario).first()
            print('ubigeo: ', persona.ubigeo)
            if persona:
                ubicacion = Ubicacion.query.filter_by(ubigeo=persona.ubigeo).first()
                print('ubicacion:', ubicacion.y)
                if ubicacion:
                    data = {
                        'distrito': ubicacion.distrito,
                        'provincia': ubicacion.provincia,
                        'ubigeo': ubicacion.ubigeo,
                        'y': ubicacion.y,
                        'x': ubicacion.x
                    }
                    return data            
        return None


historial_test_e_schema = Historial_test_e_Schema()
historiales_tests_e_schema = Historial_test_e_Schema(many=True)
