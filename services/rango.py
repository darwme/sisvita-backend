from flask import Blueprint, request, jsonify, make_response
from model.rango import Rango
from utils.db import db
from schemas.rango import rango_schema, rangos_schema

rango = Blueprint('rango', __name__)

# Crear un rango ----------------------------------------
@rango.route('/rango/v1', methods=['POST'])
def crear_rango():
    id_test = request.json.get("id_test")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    nuevo_rango = Rango(id_test, minimo, maximo, diagnostico)
    db.session.add(nuevo_rango)
    db.session.commit()

    result = rango_schema.dump(nuevo_rango)

    data = {
        'message': 'Rango creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los rangos ----------------------------------------
@rango.route('/rango/v1/listar', methods=['GET'])
def listar_rangos():
    all_rangos = Rango.query.all()
    result = rangos_schema.dump(all_rangos)

    data = {
        'message': 'Rangos recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener un rango por su ID ----------------------------------------
@rango.route('/rango/v1/<int:id>', methods=['GET'])
def obtener_rango(id):
    rango = Rango.query.get(id)

    if not rango:
        data = {
            'message': 'Rango no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = rango_schema.dump(rango)
    data = {
        'message': 'Rango recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un rango por su ID ----------------------------------------
@rango.route('/rango/v1/<int:id>', methods=['PUT'])
def actualizar_rango(id):
    rango_actual = Rango.query.get(id)

    if not rango_actual:
        data = {
            'message': 'Rango no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_test = request.json.get("id_test")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    rango_actual.id_test = id_test
    rango_actual.minimo = minimo
    rango_actual.maximo = maximo
    rango_actual.diagnostico = diagnostico

    db.session.commit()

    result = rango_schema.dump(rango_actual)

    data = {
        'message': 'Rango actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar un rango por su ID ----------------------------------------
@rango.route('/rango/v1/<int:id>', methods=['DELETE'])
def eliminar_rango(id):
    rango = Rango.query.get(id)

    if not rango:
        data = {
            'message': 'Rango no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(rango)
    db.session.commit()

    data = {
        'message': 'Rango eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
