from flask import Blueprint, request, jsonify, make_response
from model.opcion import Opcion
from utils.db import db
from schemas.opcion import opcion_schema, opciones_schema

opcion = Blueprint('opcion', __name__)

# Crear una opción ----------------------------------------
@opcion.route('/opcion/v1', methods=['POST'])
def crear_opcion():
    id_test = request.json.get("id_test")
    descripcion = request.json.get("descripcion")
    valor_opcion = request.json.get("valor_opcion")

    nueva_opcion = Opcion(id_test, descripcion, valor_opcion)
    db.session.add(nueva_opcion)
    db.session.commit()

    result = opcion_schema.dump(nueva_opcion)

    data = {
        'message': 'Opción creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las opciones ----------------------------------------
@opcion.route('/opcion/v1/listar', methods=['GET'])
def listar_opciones():
    all_opciones = Opcion.query.all()
    result = opciones_schema.dump(all_opciones)

    data = {
        'message': 'Opciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una opción por su ID ----------------------------------------
@opcion.route('/opcion/v1/<int:id>', methods=['GET'])
def obtener_opcion(id):
    opcion = Opcion.query.get(id)

    if not opcion:
        data = {
            'message': 'Opción no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = opcion_schema.dump(opcion)
    data = {
        'message': 'Opción recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

#Obtener opciones por id_test ----------------------------------------
@opcion.route('/opcion/v1/test/<int:id_test>', methods=['GET'])
def obtener_opciones_por_test(id_test):
    opciones = Opcion.query.filter_by(id_test=id_test).all()
    result = opciones_schema.dump(opciones)

    if not opciones:
        data = {
            'message': 'No se encontraron opciones para el test mencionado.',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Opciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una opción por su ID ----------------------------------------
@opcion.route('/opcion/v1/<int:id>', methods=['PUT'])
def actualizar_opcion(id):
    opcion_actual = Opcion.query.get(id)

    if not opcion_actual:
        data = {
            'message': 'Opción no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_test = request.json.get("id_test")
    descripcion = request.json.get("descripcion")
    valor_opcion = request.json.get("valor_opcion")

    opcion_actual.id_test = id_test
    opcion_actual.descripcion = descripcion
    opcion_actual.valor_opcion = valor_opcion

    db.session.commit()

    result = opcion_schema.dump(opcion_actual)

    data = {
        'message': 'Opción actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una opción por su ID ----------------------------------------
@opcion.route('/opcion/v1/<int:id>', methods=['DELETE'])
def eliminar_opcion(id):
    opcion = Opcion.query.get(id)

    if not opcion:
        data = {
            'message': 'Opción no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(opcion)
    db.session.commit()

    data = {
        'message': 'Opción eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)


# Listar opciones por id_test ----------------------------------------
@opcion.route('/opcion/v1/test/<int:id_test>', methods=['GET'])
def listar_opciones_por_test(id_test):
    opciones = Opcion.query.filter_by(id_test=id_test).all()

    result = opciones_schema.dump(opciones)

    if not opciones:
        data = {
            'message': 'No se encontraron opciones para el id_test especificado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Opciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)