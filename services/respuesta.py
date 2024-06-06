from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.respuesta import Respuesta
from utils.db import db
from schemas.respuesta import RespuestaSchema

respuesta= Blueprint('respuesta', __name__)

@respuesta.route('/respuesta', methods=['POST'])
@jwt_required()
def add_respuesta():
    id_respuesta = request.json.get('id_respuesta')
    id_cuestionario = request.json.get('id_cuestionario')
    id_fila = request.json.get('id_fila')
    valor = request.json.get('valor')

    nueva_respuesta = Respuesta(id_respuesta,id_cuestionario,id_fila,valor)
    db.session.add(nueva_respuesta)
    db.session.commit()

    respuesta_schema = RespuestaSchema()
    result = respuesta_schema.dump(nueva_respuesta)

    data = {
        'message': 'Respuesta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@respuesta.route('/respuesta/<int:id>', methods=['GET'])
@jwt_required()
def get_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    respuesta_schema = RespuestaSchema()
    result = respuesta_schema.dump(respuesta)

    data = {
        'message': 'Respuesta recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuesta.route('/respuesta', methods=['GET'])
@jwt_required()
def get_respuestas():
    respuestas = Respuesta.query.all()

    respuestas_schema = RespuestaSchema(many=True)
    result = respuestas_schema.dump(respuestas)

    data = {
        'message': 'Respuestas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuesta.route('/respuesta/<int:id>', methods=['PUT'])
@jwt_required()
def update_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    respuesta.id_respuesta = request.json.get('id_respuesta')
    respuesta.id_cuestionario = request.json.get('id_cuestionario')
    respuesta.id_fila = request.json.get('id_fila')
    respuesta.valor = request.json.get('valor')

    db.session.commit()

    respuesta_schema = RespuestaSchema()
    result = respuesta_schema.dump(respuesta)

    data = {
        'message': 'Respuesta actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuesta.route('/respuesta/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(respuesta)
    db.session.commit()

    data = {
        'message': 'Respuesta eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
