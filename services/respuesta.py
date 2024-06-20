from flask import Blueprint, request, jsonify, make_response
from model.respuesta import Respuesta  # Asegúrate de importar el modelo correcto
from utils.db import db
from schemas.respuesta import respuesta_schema, respuestas_schema

respuesta = Blueprint('respuesta', __name__)

# Crear una respuesta ----------------------------------------
@respuesta.route('/respuesta/v1', methods=['POST'])
def crear_respuesta():
    id_historial_test = request.json.get("id_historial_test")
    id_pregunta = request.json.get("id_pregunta")
    valor = request.json.get("valor")

    nueva_respuesta = Respuesta(id_historial_test,id_pregunta,valor)
    db.session.add(nueva_respuesta)
    db.session.commit()

    result = respuesta_schema.dump(nueva_respuesta)

    data = {
        'message': 'Respuesta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las respuestas ----------------------------------------
@respuesta.route('/respuesta/v1/listar', methods=['GET'])
def listar_respuestas():
    all_respuestas = Respuesta.query.all()
    result = respuestas_schema.dump(all_respuestas)

    data = {
        'message': 'Respuestas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una respuesta por su ID ----------------------------------------
@respuesta.route('/respuesta/v1/<int:id>', methods=['GET'])
def obtener_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = respuesta_schema.dump(respuesta)
    data = {
        'message': 'Respuesta recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una respuesta por su ID ----------------------------------------
@respuesta.route('/respuesta/v1/<int:id>', methods=['PUT'])
def actualizar_respuesta(id):
    respuesta_actual = Respuesta.query.get(id)

    if not respuesta_actual:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_historial_test = request.json.get("id_historial_test")
    id_pregunta = request.json.get("id_pregunta")
    valor = request.json.get("valor")

    respuesta_actual.id_historial_test = id_historial_test
    respuesta_actual.id_pregunta = id_pregunta
    respuesta_actual.valor = valor

    db.session.commit()

    result = respuesta_schema.dump(respuesta_actual)

    data = {
        'message': 'Respuesta actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una respuesta por su ID ----------------------------------------
@respuesta.route('/respuesta/v1/<int:id>', methods=['DELETE'])
def eliminar_respuesta(id):
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
