from flask import Blueprint, request, jsonify, make_response
from model.evaluacion import Evaluacion
from utils.db import db
from schemas.evaluacion import evaluacion_schema, evaluaciones_schema
from datetime import datetime
from model.historial_test import Historial_test
from model.usuario import Usuario
from model.persona import Persona
from model.paciente import Paciente
from model.especialista import Especialista
from model.evaluacion import Evaluacion
from schemas.evaluacion import evaluaciones_schema

gestor_evaluacion = Blueprint('gestor_evaluacion', __name__)


# Crear una evaluación basada en el codigo_historial_test
@gestor_evaluacion.route('/gestor_evaluacion/v1/crear_evaluacion/<string:codigo_historial_test>/<string:codigo_especialista>', methods=['POST'])
def crear_evaluacion_por_codigo(codigo_historial_test, codigo_especialista):
    try:
        # Buscar el historial de test por el código
        historial = Historial_test.query.filter_by(codigo_historial_test=codigo_historial_test).first()
        
        if not historial:
            return make_response(jsonify({
                'message': 'Historial de test no encontrado con el código proporcionado',
                'status': 404
            }), 404)
            
        historial.estado= "evaluado"

        # Buscar el especialista por el código
        especialista = Especialista.query.filter_by(codigo_especialista=codigo_especialista).first()

        if not especialista:
            return make_response(jsonify({
                'message': 'Especialista no encontrado con el código proporcionado',
                'status': 404
            }), 404)

        # Buscar el usuario asociado al historial de test
        usuario = Usuario.query.filter_by(id_usuario=historial.id_usuario).first()

        if not usuario:
            return make_response(jsonify({
                'message': 'Usuario no encontrado con el ID proporcionado en el historial de test',
                'status': 404
            }), 404)

        # Buscar la persona asociada al usuario
        persona = Persona.query.filter_by(id_usuario=usuario.id_usuario).first()

        if not persona:
            return make_response(jsonify({
                'message': 'Persona no encontrada asociada al usuario',
                'status': 404
            }), 404)

        # Buscar el paciente asociado a la persona
        paciente = Paciente.query.filter_by(id_persona=persona.id_persona).first()

        if not paciente:
            return make_response(jsonify({
                'message': 'Paciente no encontrado con el ID proporcionado en la persona',
                'status': 404
            }), 404)

        # Extraer datos de la solicitud
        data = request.json
        fecha_evaluacion = datetime.now()

        # Crear una nueva evaluación
        nueva_evaluacion = Evaluacion(
            id_especialista=especialista.id_especialista,
            id_historial_test=historial.id_historial_test,
            id_paciente=paciente.id_paciente,  # Usar el id_paciente obtenido a través de las relaciones
            fecha_evaluacion=fecha_evaluacion,
            fundamento_cientifico=data.get("fundamento_cientifico"),
            tratamiento=data.get("tratamiento"),
            descripcion_tratamiento=data.get("descripcion_tratamiento"),
            comunicacion=data.get("comunicacion")
        )

        # Guardar la nueva evaluación en la base de datos
        db.session.add(nueva_evaluacion)
        db.session.commit()

        # Serializar la nueva evaluación
        result = evaluacion_schema.dump(nueva_evaluacion)

        return make_response(jsonify({
            'message': 'Evaluación creada correctamente basada en el código del historial de test y código del especialista',
            'status': 201,
            'data': result
        }), 201)
    
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({
            'message': f'Error al crear la evaluación: {str(e)}',
            'status': 500
        }), 500)


@gestor_evaluacion.route('/gestor_evaluacion/v1/ver_evaluacion/<string:codigo_historial_test>', methods=['GET'])
def obtener_evaluaciones_por_historial(codigo_historial_test):
    try:
        # Buscar el historial de test por el código
        historial = Historial_test.query.filter_by(codigo_historial_test=codigo_historial_test).first()

        if not historial:
            return make_response(jsonify({
                'message': f'No se encontró historial de test con código {codigo_historial_test}',
                'status': 404
            }), 404)

        # Obtener todas las evaluaciones asociadas al id_historial_test
        evaluaciones = Evaluacion.query.filter_by(id_historial_test=historial.id_historial_test).all()

        if not evaluaciones:
            return make_response(jsonify({
                'message': f'No se encontraron evaluaciones para el historial de test con código {codigo_historial_test}',
                'status': 404
            }), 404)

        # Serializar las evaluaciones
        result = evaluaciones_schema.dump(evaluaciones)

        return make_response(jsonify(result), 200)

    except Exception as e:
        return make_response(jsonify({
            'message': f'Error al obtener las evaluaciones: {str(e)}',
            'status': 500
        }), 500)
