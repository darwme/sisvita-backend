from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.respuesta import Respuesta
from utils.db import db
from schemas.respuesta import respuesta_schema, respuestas_schema

respuesta_routes = Blueprint('respuesta', __name__)  # Crea un blueprint llamado 'respuesta'

# Crear un nuevo repuesta -----------------------------------------
@respuesta_routes.route('/respuesta/v1', methods=['POST'])
@jwt_required()
def crear_respuesta():
    id_fila = request.json.get("id_fila")
    id_test = request.json.get("id_test")
    valor = request.json.get("valor")
        
    nueva_respuesta = Respuesta(id_fila,id_test,valor)
    db.session.add(nueva_respuesta)
    db.session.commit()

    result = respuesta_schema.dump(nueva_respuesta)

    data = {
        'message': 'Respuesta creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)


# Listar todos los respuestas -----------------------------------------
@respuesta_routes.route('/respuesta/v1/listar', methods=['GET'])
@jwt_required()
def listar_respuestas():
    all_respuestas = Respuesta.query.all()
    result = respuestas_schema.dump(all_respuestas)

    data = {
        'message': 'Respuestas recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


# Obtener un respuesta por su ID -----------------------------------------
@respuesta_routes.route('/respuesta/v1/<int:id>', methods=['GET'])
@jwt_required()
def obtener_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = respuesta_schema.dump(respuesta)

    data = {
        'message': 'Respuesta recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un respuesta por su ID -----------------------------------------
@respuesta_routes.route('/respuesta/v1/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_respuesta(id):
    nueva_respuesta = Respuesta.query.get(id)

    if not nueva_respuesta:
        data = {
            'message': 'Respuesta no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_respuesta = request.json.get("id_respuesta")
    id_fila = request.json.get("id_fila")
    id_test = request.json.get("id_test")
    valor = request.json.get("valor")
        
    
    nueva_respuesta.id_respuesta = id_respuesta
    nueva_respuesta.id_fila = id_fila
    nueva_respuesta.id_test = id_test
    nueva_respuesta.valor = valor

    db.session.commit()

    result = respuestas_schema.dump(nueva_respuesta)

    data = {
        'message': 'respuesta actualizada correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)


# Eliminar una respuesta por su ID -------------------------------------------
@respuesta_routes.route('/respuesta/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_respuesta(id):

    vieja_respuesta = Respuesta.query.get(id)

    if not vieja_respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(vieja_respuesta)
    db.session.commit()

    data = {
        'message': 'respuesta eliminada correctamente',
        'status': 202
    }

    return make_response(jsonify(data), 202)