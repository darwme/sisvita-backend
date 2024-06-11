from flask import Blueprint, request, jsonify, make_response
from model.pregunta import Pregunta
from utils.db import db
from schemas.pregunta import pregunta_schema, preguntas_schema

pregunta = Blueprint('pregunta', __name__)

# Crear una pregunta
@pregunta.route('/pregunta/v1', methods=['POST'])
def crear_pregunta():
    id_pregunta = request.json.get("id_pregunta")
    enunciado = request.json.get("enunciado")

    nueva_pregunta = Pregunta(id_pregunta=id_pregunta, enunciado=enunciado)
    db.session.add(nueva_pregunta)
    db.session.commit()

    result = pregunta_schema.dump(nueva_pregunta)

    data = {
        'message': 'Pregunta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las preguntas
@pregunta.route('/pregunta/v1/listar', methods=['GET'])
def listar_preguntas():
    all_preguntas = Pregunta.query.all()
    result = preguntas_schema.dump(all_preguntas)

    data = {
        'message': 'Preguntas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una pregunta por su ID
@pregunta.route('/pregunta/v1/<int:id>', methods=['GET'])
def obtener_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = pregunta_schema.dump(pregunta)
    data = {
        'message': 'Pregunta recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una pregunta por su ID
@pregunta.route('/pregunta/v1/<int:id>', methods=['PUT'])
def actualizar_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_pregunta = request.json.get("id_pregunta")
    enunciado = request.json.get("enunciado")

    pregunta.id_pregunta = id_pregunta
    pregunta.enunciado = enunciado

    db.session.commit()

    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una pregunta por su ID
@pregunta.route('/pregunta/v1/<int:id>', methods=['DELETE'])
def eliminar_pregunta(id):
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
