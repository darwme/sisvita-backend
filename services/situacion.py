from flask import Blueprint, request, jsonify, make_response
from model.situacion import Situacion
from model.seccion import Seccion
from utils.db import db
from schemas.situacion import situacion_schema, situaciones_schema

situacion = Blueprint('situacion', __name__)

# Crear una situación
@situacion.route('/situacion/v1', methods=['POST'])
def crear_situacion():
    id_situacion = request.json.get("id_situacion")
    id_seccion = request.json.get("id_seccion")
    enunciado = request.json.get("enunciado")

    seccion = Seccion.query.get(id_seccion)
    if not seccion:
        return make_response(jsonify({'message': 'Sección no encontrada', 'status': 404}), 404)

    nueva_situacion = Situacion(id_situacion=id_situacion, id_seccion=id_seccion, enunciado=enunciado)
    db.session.add(nueva_situacion)
    db.session.commit()

    result = situacion_schema.dump(nueva_situacion)

    data = {
        'message': 'Situación creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las situaciones
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

# Obtener una situación por su ID
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

# Actualizar una situación por su ID
@situacion.route('/situacion/v1/<int:id>', methods=['PUT'])
def actualizar_situacion(id):
    situacion = Situacion.query.get(id)

    if not situacion:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_situacion = request.json.get("id_situacion")
    id_seccion = request.json.get("id_seccion")
    enunciado = request.json.get("enunciado")

    seccion = Seccion.query.get(id_seccion)
    if not seccion:
        return make_response(jsonify({'message': 'Sección no encontrada', 'status': 404}), 404)

    situacion.id_situacion = id_situacion
    situacion.id_seccion = id_seccion
    situacion.enunciado = enunciado

    db.session.commit()

    result = situacion_schema.dump(situacion)

    data = {
        'message': 'Situación actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una situación por su ID
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
