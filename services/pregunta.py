from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.pregunta import Pregunta
from utils.db import db
from schemas.pregunta import PreguntaSchema

pregunta = Blueprint('pregunta', __name__)

@pregunta.route('/pregunta', methods=['POST'])
@jwt_required()
def add_pregunta():
    id_pregunta = request.json.get('id_pregunta')
    enunciado = request.json.get('enunciado')

    nueva_pregunta = Pregunta(id_pregunta,enunciado)
    db.session.add(nueva_pregunta)
    db.session.commit()

    pregunta_schema = PreguntaSchema()
    result = pregunta_schema.dump(nueva_pregunta)

    data = {
        'message': 'Pregunta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@pregunta.route('/pregunta/<int:id>', methods=['GET'])
@jwt_required()
def get_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    pregunta_schema = PreguntaSchema()
    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta.route('/pregunta', methods=['GET'])
@jwt_required()
def get_preguntas():
    preguntas = Pregunta.query.all()

    preguntas_schema = PreguntaSchema(many=True)
    result = preguntas_schema.dump(preguntas)

    data = {
        'message': 'Preguntas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta.route('/pregunta/<int:id>', methods=['PUT'])
@jwt_required()
def update_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    pregunta.id_pregunta = request.json.get('id_pregunta')
    pregunta.enunciado = request.json.get('enunciado')

    db.session.commit()

    pregunta_schema = PreguntaSchema()
    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta.route('/pregunta/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(pregunta)
    db.session.commit()

    data = {
        'message': 'Pregunta eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
