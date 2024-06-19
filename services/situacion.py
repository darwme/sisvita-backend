from flask import Blueprint, request, jsonify, make_response
from model.situacion import Situacion
from utils.db import db
from schemas.situacion import situacion_schema, situaciones_schema

situacion = Blueprint('situacion', __name__)

# Crear una situación ----------------------------------------
@situacion.route('/situacion/v1', methods=['POST'])
def crear_situacion():
    id_seccion = request.json.get("id_seccion")
    descripcion = request.json.get("descripcion")
    cant_preguntas = request.json.get("cant_preguntas")

    nueva_situacion = Situacion(id_seccion, descripcion, cant_preguntas)
    db.session.add(nueva_situacion)
    db.session.commit()

    result = situacion_schema.dump(nueva_situacion)

    data = {
        'message': 'Situación creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las situaciones ----------------------------------------
@situacion.route('/situacion/v1/listar', methods=['GET'])
def listar_situaciones():
    all_situaciones = Situacion.query.all()
    result = situaciones_schema.dump(all_situaciones)

    data = {
        'message': 'Situaciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una situación por su ID ----------------------------------------
@situacion.route('/situacion/v1/<int:id>', methods=['GET'])
def obtener_situacion(id):
    situacion = Situacion.query.get(id)

    if not situacion:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = situacion_schema.dump(situacion)
    data = {
        'message': 'Situación recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una situación por su ID ----------------------------------------
@situacion.route('/situacion/v1/<int:id>', methods=['PUT'])
def actualizar_situacion(id):
    situacion_actual = Situacion.query.get(id)

    if not situacion_actual:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_seccion = request.json.get("id_seccion")
    descripcion = request.json.get("descripcion")
    cant_preguntas = request.json.get("cant_preguntas")

    situacion_actual.id_seccion = id_seccion
    situacion_actual.descripcion = descripcion
    situacion_actual.cant_preguntas = cant_preguntas

    db.session.commit()

    result = situacion_schema.dump(situacion_actual)

    data = {
        'message': 'Situación actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una situación por su ID ----------------------------------------
@situacion.route('/situacion/v1/<int:id>', methods=['DELETE'])
def eliminar_situacion(id):
    situacion = Situacion.query.get(id)

    if not situacion:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(situacion)
    db.session.commit()

    data = {
        'message': 'Situación eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
