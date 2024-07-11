from flask import Blueprint, request, jsonify, make_response
from model.rango_seccion import Rango_seccion
from utils.db import db
from schemas.rango_seccion import rango_seccion_schema, rango_secciones_schema

rango_seccion = Blueprint('rango_seccion', __name__)

# Crear un rango_seccion ----------------------------------------
@rango_seccion.route('/rango_seccion/v1', methods=['POST'])
def crear_rango_seccion():
    id_seccion = request.json.get("id_seccion")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    nuevo_rango_seccion = rango_seccion(id_seccion, minimo, maximo, diagnostico)
    db.session.add(nuevo_rango_seccion)
    db.session.commit()

    result = rango_seccion_schema.dump(nuevo_rango_seccion)

    data = {
        'message': 'rango_seccion creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los rango_seccions ----------------------------------------
@rango_seccion.route('/rango_seccion/v1/listar', methods=['GET'])
def listar_rango_seccions():
    all_rango_secciones = Rango_seccion.query.all()
    result = rango_secciones_schema.dump(all_rango_secciones)

    return make_response(jsonify(result), 200)

# Obtener un rango_seccion por su ID ----------------------------------------
@rango_seccion.route('/rango_seccion/v1/<int:id>', methods=['GET'])
def obtener_rango_seccion(id):
    rango_seccion = Rango_seccion.query.get(id)

    if not rango_seccion:
        data = {
            'message': 'rango_seccion no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = rango_seccion_schema.dump(rango_seccion)
    data = {
        'message': 'rango_seccion recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un rango_seccion por su ID ----------------------------------------
@rango_seccion.route('/rango_seccion/v1/<int:id>', methods=['PUT'])
def actualizar_rango_seccion(id):
    rango_seccion_actual = Rango_seccion.query.get(id)

    if not rango_seccion_actual:
        data = {
            'message': 'rango_seccion no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_seccion = request.json.get("id_seccion")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    rango_seccion_actual.id_seccion = id_seccion
    rango_seccion_actual.minimo = minimo
    rango_seccion_actual.maximo = maximo
    rango_seccion_actual.diagnostico = diagnostico

    db.session.commit()

    result = rango_seccion_schema.dump(rango_seccion_actual)

    data = {
        'message': 'rango_seccion actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar un rango_seccion por su ID ----------------------------------------
@rango_seccion.route('/rango_seccion/v1/<int:id>', methods=['DELETE'])
def eliminar_rango_seccion(id):
    rango_seccion = Rango_seccion.query.get(id)

    if not rango_seccion:
        data = {
            'message': 'rango_seccion no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(rango_seccion)
    db.session.commit()

    data = {
        'message': 'rango_seccion eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)

# Listar rango_secciones por id seccion----------------------------------------
@rango_seccion.route('/rango_seccion/v1/test/<int:id_seccion>', methods=['GET'])
def listar_rango_secciones_por_seccion(id_seccion):
    rango_secciones = Rango_seccion.query.filter_by(id_seccion=id_seccion).all()

    result = rango_secciones_schema.dump(rango_secciones)

    if not rango_secciones:
        data = {
            'message': 'No se encontraron rango_seccions para el id_test proporcionado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'rango_seccions recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)