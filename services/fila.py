from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.fila import Fila
from utils.db import db
from schemas.fila import FilaSchema

fila = Blueprint('fila', __name__)

@fila.route('/fila/', methods=['POST'])
@jwt_required()
def add_fila():
    id_fila = request.json.get('id_fila')
    id_pregunta = request.json.get('id_pregunta')
    id_situacion = request.json.get('id_situacion')

    nueva_fila = Fila(id_fila,id_pregunta, id_situacion)
    db.session.add(nueva_fila)
    db.session.commit()

    fila_schema = FilaSchema()
    result = fila_schema.dump(nueva_fila)

    data = {
        'message': 'Fila creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@fila.route('/fila/<int:id>', methods=['GET'])
@jwt_required()
def get_fila(id):
    fila = Fila.query.get(id)

    if not fila:
        data = {
            'message': 'Fila no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    fila_schema = FilaSchema()
    result = fila_schema.dump(fila)

    data = {
        'message': 'Fila recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@fila.route('/fila', methods=['GET'])
@jwt_required()
def get_filas():
    filas = Fila.query.all()

    filas_schema = FilaSchema(many=True)
    result = filas_schema.dump(filas)

    data = {
        'message': 'Filas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@fila.route('/fila/<int:id>', methods=['PUT'])
@jwt_required()
def update_fila(id):
    fila = Fila.query.get(id)

    if not fila:
        data = {
            'message': 'Fila no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    fila.id_fila = request.json.get('id_fila')
    fila.id_pregunta = request.json.get('id_pregunta')
    fila.id_situacion = request.json.get('id_situacion')

    db.session.commit()

    fila_schema = FilaSchema()
    result = fila_schema.dump(fila)

    data = {
        'message': 'Fila actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@fila.route('/fila/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_fila(id):
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
