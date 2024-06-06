from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.situacion import Situacion
from utils.db import db
from schemas.situacion import SituacionSchema

situacion = Blueprint('situacion', __name__)

@situacion.route('/situacion', methods=['POST'])
@jwt_required()
def add_situacion():
    id_situacion = request.json.get('id_situacion')
    seccion = request.json.get('seccion')
    enunciado = request.json.get('enunciado')

    nueva_situacion = Situacion(id_situacion,seccion,enunciado)
    db.session.add(nueva_situacion)
    db.session.commit()

    situacion_schema = SituacionSchema()
    result = situacion_schema.dump(nueva_situacion)

    data = {
        'message': 'Situación creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@situacion.route('/situacion/<int:id>', methods=['GET'])
@jwt_required()
def get_situacion(id):
    situacion = Situacion.query.get(id)

    if not situacion:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    situacion_schema = SituacionSchema()
    result = situacion_schema.dump(situacion)

    data = {
        'message': 'Situación recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@situacion.route('/situacion', methods=['GET'])
@jwt_required()
def get_situaciones():
    situaciones = Situacion.query.all()

    situaciones_schema = SituacionSchema(many=True)
    result = situaciones_schema.dump(situaciones)

    data = {
        'message': 'Situaciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@situacion.route('/situacion/<int:id>', methods=['PUT'])
@jwt_required()
def update_situacion(id):
    situacion = Situacion.query.get(id)

    if not situacion:
        data = {
            'message': 'Situación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    situacion.id_situacion = request.json.get('id_situacion')
    situacion.seccion = request.json.get('seccion')
    situacion.enunciado = request.json.get('enunciado')

    db.session.commit()

    situacion_schema = SituacionSchema()
    result = situacion_schema.dump(situacion)

    data = {
        'message': 'Situación actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@situacion.route('/situacion/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_situacion(id):
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
