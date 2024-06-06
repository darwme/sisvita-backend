from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.clasificacion import Clasificacion
from utils.db import db
from schemas.clasificacion import ClasificacionSchema

clasificacion = Blueprint('clasificacion', __name__)

@clasificacion.route('/clasificacion/', methods=['POST'])
@jwt_required()
def add_clasificacion():
    id_clasificacion=request.json.get('id_clasificacion')
    nombre = request.json.get('nombre')
    categoria = request.json.get('categoria')
    minimo = request.json.get('minimo')
    maximo = request.json.get('maximo')
    sexo = request.json.get('sexo')

    nueva_clasificacion = Clasificacion(id_clasificacion,nombre, categoria, minimo, maximo,sexo)
    db.session.add(nueva_clasificacion)
    db.session.commit()

    clasificacion_schema = ClasificacionSchema()
    result = clasificacion_schema.dump(nueva_clasificacion)

    data = {
        'message': 'Clasificación creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@clasificacion.route('/clasificacion/<int:id>', methods=['GET'])
@jwt_required()
def get_clasificacion(id):
    clasificacion = Clasificacion.query.get(id)

    if not clasificacion:
        data = {
            'message': 'Clasificación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    clasificacion_schema = ClasificacionSchema()
    result = clasificacion_schema.dump(clasificacion)

    data = {
        'message': 'Clasificación recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@clasificacion.route('/clasificacion', methods=['GET'])
@jwt_required()
def get_clasificaciones():
    clasificaciones = Clasificacion.query.all()

    clasificaciones_schema = ClasificacionSchema(many=True)
    result = clasificaciones_schema.dump(clasificaciones)

    data = {
        'message': 'Clasificaciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@clasificacion.route('/clasificacion/<int:id>', methods=['PUT'])
@jwt_required()
def update_clasificacion(id):
    clasificacion = Clasificacion.query.get(id)

    if not clasificacion:
        data = {
            'message': 'Clasificación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    clasificacion.id_clasificacion=request.json.get('id_clasificacion')
    clasificacion.nombre = request.json.get('nombre')
    clasificacion.categoria = request.json.get('categoria')
    clasificacion.minimo = request.json.get('minimo')
    clasificacion.maximo = request.json.get('maximo')
    clasificacion.sexo = request.json.get('sexo')

    db.session.commit()

    clasificacion_schema = ClasificacionSchema()
    result = clasificacion_schema.dump(clasificacion)

    data = {
        'message': 'Clasificación actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@clasificacion.route('/clasificacion/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_clasificacion(id):
    clasificacion = Clasificacion.query.get(id)

    if not clasificacion:
        data = {
            'message': 'Clasificación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(clasificacion)
    db.session.commit()

    data = {
        'message': 'Clasificación eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
