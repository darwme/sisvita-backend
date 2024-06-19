from flask import Blueprint, request, jsonify, make_response
from model.seccion import Seccion
from utils.db import db
from schemas.seccion import seccion_schema, secciones_schema

seccion = Blueprint('seccion', __name__)

# Crear una sección ----------------------------------------
@seccion.route('/seccion/v1', methods=['POST'])
def crear_seccion():
    id_test = request.json.get("id_test")
    descripcion = request.json.get("descripcion")
    cant_situaciones = request.json.get("cant_situaciones")

    nueva_seccion = Seccion(id_test,descripcion,cant_situaciones)
    db.session.add(nueva_seccion)
    db.session.commit()

    result = seccion_schema.dump(nueva_seccion)

    data = {
        'message': 'Sección creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las secciones ----------------------------------------
@seccion.route('/seccion/v1/listar', methods=['GET'])
def listar_secciones():
    all_secciones = Seccion.query.all()
    result = secciones_schema.dump(all_secciones)

    data = {
        'message': 'Secciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una sección por su ID ----------------------------------------
@seccion.route('/seccion/v1/<int:id>', methods=['GET'])
def obtener_seccion(id):
    seccion = Seccion.query.get(id)

    if not seccion:
        data = {
            'message': 'Sección no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = seccion_schema.dump(seccion)
    data = {
        'message': 'Sección recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una sección por su ID ----------------------------------------
@seccion.route('/seccion/v1/<int:id>', methods=['PUT'])
def actualizar_seccion(id):
    nueva_seccion = Seccion.query.get(id)

    if not nueva_seccion:
        data = {
            'message': 'Sección no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_test = request.json.get("id_test")
    descripcion = request.json.get("descripcion")
    cant_situaciones = request.json.get("cant_situaciones")

    nueva_seccion.id_test = id_test
    nueva_seccion.descripcion = descripcion
    nueva_seccion.cant_situaciones = cant_situaciones

    db.session.commit()

    result = seccion_schema.dump(nueva_seccion)

    data = {
        'message': 'Sección actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una sección por su ID ----------------------------------------
@seccion.route('/seccion/v1/<int:id>', methods=['DELETE'])
def eliminar_seccion(id):
    seccion = Seccion.query.get(id)

    if not seccion:
        data = {
            'message': 'Sección no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(seccion)
    db.session.commit()

    data = {
        'message': 'Sección eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)