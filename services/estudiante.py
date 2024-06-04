from flask import Blueprint, request, jsonify, make_response
from model.estudiante import Estudiante
from utils.db import db
from schemas.estudiante import estudiante_schema, estudiantes_schema
from schemas.test import test_schema, tests_schema

estudiante = Blueprint('estudiante', __name__)

@estudiante.route('/estudiante/v1/tests/<int:id_estudiante>', methods=['GET'])
def getTests(id_estudiante):

    estudiante = Estudiante.query.get(id_estudiante)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    tests = estudiante.getTests()

    result = tests_schema.dump(tests)

    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante.route('/estudiante/v1/test/<int:id_test>', methods=['GET'])
def getTest(id_test):

    id_estudiante = request.json.get("id_estudiante")

    estudiante = Estudiante.query.get(id_estudiante)
    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    test = estudiante.getTestByIdEstudiante(id_test)
    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    result = test_schema.dump(test)
    data = {
        'message': 'Test recuperado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@estudiante.route('/estudiante/v1/listar', methods=['GET'])
def getEstudiantes():
    estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(estudiantes)

    data = {
        'message': 'Estudiantes recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante.route('/estudiante/v1/<int:id>', methods=['GET'])
def getOne(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = estudiante_schema.dump(estudiante)
    data = {
        'message': 'Estudiante recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante.route('/estudiante/v1/<int:id>', methods=['PUT'])
def updateEstudiante(id):
    nuevo_estudiante = Estudiante.query.get(id)

    if not nuevo_estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_estudiante = request.json.get("id_estudiante")
    id_usuario = request.json.get("id_usuario")
    codigo_estudiante = request.json.get("codigo_estudiante")
    carrera_profesional = request.json.get("carrera_profesional")

    nuevo_estudiante.id_estudiante = id_estudiante
    nuevo_estudiante.id_usuario = id_usuario
    nuevo_estudiante.codigo_estudiante = codigo_estudiante
    nuevo_estudiante.carrera_profesional = carrera_profesional

    db.session.commit()

    result = estudiante_schema.dump(nuevo_estudiante)

    data = {
        'message': 'Estudiante actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante.route('/estudiante/v1/<int:id>', methods=['DELETE'])
def deleteOne(id):

    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(estudiante)
    db.session.commit()

    data = {
        'message': 'Estudiante eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)