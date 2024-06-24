from flask import Blueprint, request, jsonify, make_response
from model.seccion import Seccion_respuesta
from utils.db import db
from schemas.seccion import seccion_respuesta_schema, seccion_respuestas_schema

seccion_respuesta = Blueprint('seccion_respuesta', __name__)

# Crear una sección_respuesta ----------------------------------------
@seccion_respuesta.route('/seccion_respuesta/v1', methods=['POST'])
def crear_seccion_respuesta():
    id_usuario = request.json.get("id_usuario")
    id_test = request.json.get("id_test")
    id_seccion = request.json.get("id_seccion")
    respuestas = request.json.get("respuestas")

    nueva_seccion_respuesta = Seccion_respuesta(id_usuario,id_test,id_seccion,respuestas)
    db.session.add(nueva_seccion_respuesta)
    db.session.commit()

    result = seccion_respuesta_schema.dump(nueva_seccion_respuesta)

    data = {
        'message': 'Sección_respuesta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las secciones_respuestas ----------------------------------------
@seccion_respuesta.route('/seccion_respuesta/v1/listar', methods=['GET'])
def listar_secciones_respuestas():
    all_secciones_respuestas = Seccion_respuesta.query.all()
    result = seccion_respuestas_schema.dump(all_secciones_respuestas)

    data = {
        'message': 'Secciones_respuestas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

#Obtener secciones_respuestas por id_seccion ----------------------------------------

@seccion_respuesta.route('/seccion_respuesta/v1/seccion/<int:id_seccion>', methods=['GET'])
def obtener_secciones(id_seccion):
    seccion_respuestas = Seccion_respuesta.query.filter_by(id_seccion=id_seccion).all()
    
    result = seccion_respuestas_schema.dump(seccion_respuestas)

    if not seccion_respuestas:
        data = {
            'message': 'Secciones_respuestas no encontradas',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Secciones_respuestas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


# Obtener una sección_respuestas por su ID ----------------------------------------
@seccion_respuesta.route('/seccion_respuesta/v1/<int:id>', methods=['GET'])
def obtener_seccion_respuesta(id):
    seccion_respuesta = Seccion_respuesta.query.get(id)

    if not seccion_respuesta:
        data = {
            'message': 'Sección_respuestas no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = seccion_respuesta_schema.dump(seccion_respuesta)
    data = {
        'message': 'Sección respuestas recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una sección respuesta por su ID ----------------------------------------
@seccion_respuesta.route('/seccion_respuesta/v1/<int:id>', methods=['PUT'])
def actualizar_seccion_respuesta(id):
    nueva_seccion_respuesta = Seccion_respuesta.query.get(id)

    if not nueva_seccion_respuesta:
        data = {
            'message': 'Sección respuesta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_usuario = request.json.get("id_usuario")
    id_test = request.json.get("id_test")
    id_seccion = request.json.get("id_seccion")
    respuestas = request.json.get("respuestas")

    nueva_seccion_respuesta.id_usuario = id_usuario
    nueva_seccion_respuesta.id_test = id_test
    nueva_seccion_respuesta.id_seccion = id_seccion
    nueva_seccion_respuesta.respuestas = respuestas

    db.session.commit()

    result = seccion_respuesta_schema.dump(nueva_seccion_respuesta)

    data = {
        'message': 'Sección respuesta actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una sección respuesata por su ID ----------------------------------------
@seccion_respuesta.route('/seccion_respuesta/v1/<int:id>', methods=['DELETE'])
def eliminar_seccion(id):
    seccion_respuesta = Seccion_respuesta.query.get(id)

    if not seccion_respuesta:
        data = {
            'message': 'Sección respuesta no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(seccion_respuesta)
    db.session.commit()

    data = {
        'message': 'Sección respuesta eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)