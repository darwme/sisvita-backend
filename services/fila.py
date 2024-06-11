from flask import Blueprint, request, jsonify, make_response
from model.fila import Fila
from utils.db import db
from schemas.fila import fila_schema, filas_schema

fila = Blueprint('fila', __name__)

# Crear una fila
@fila.route('/fila/v1', methods=['POST'])
def crear_fila():
    id_fila = request.json.get("id_fila")
    id_pregunta = request.json.get("id_pregunta")
    id_situacion = request.json.get("id_situacion")

    nueva_fila = Fila(id_fila=id_fila, id_pregunta=id_pregunta, id_situacion=id_situacion)
    db.session.add(nueva_fila)
    db.session.commit()

    result = fila_schema.dump(nueva_fila)

    data = {
        'message': 'Fila creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las filas
@fila.route('/fila/v1/listar', methods=['GET'])
def listar_filas():
    all_filas = Fila.query.all()
    result = filas_schema.dump(all_filas)

    data = {
        'message': 'Filas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una fila por su ID
@fila.route('/fila/v1/<int:id>', methods=['GET'])
def obtener_fila(id):
    fila = Fila.query.get(id)

    if not fila:
        data = {
            'message': 'Fila no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = fila_schema.dump(fila)
    data = {
        'message': 'Fila recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una fila por su ID
@fila.route('/fila/v1/<int:id>', methods=['PUT'])
def actualizar_fila(id):
    fila = Fila.query.get(id)

    if not fila:
        data = {
            'message': 'Fila no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_fila = request.json.get("id_fila")
    id_pregunta = request.json.get("id_pregunta")
    id_situacion = request.json.get("id_situacion")

    fila.id_fila = id_fila
    fila.id_pregunta = id_pregunta
    fila.id_situacion = id_situacion

    db.session.commit()

    result = fila_schema.dump(fila)

    data = {
        'message': 'Fila actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una fila por su ID
@fila.route('/fila/v1/<int:id>', methods=['DELETE'])
def eliminar_fila(id):
    fila = Fila.query.get(id)

    if not fila:
        data = {
            'message': 'Fila no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(fila)
    db.session.commit()

    data = {
        'message': 'Fila eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
