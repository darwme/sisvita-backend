from flask import Blueprint, request, jsonify, make_response
from model.rango_test import Rango_test
from utils.db import db
from schemas.rango_test import rango_test_schema, rango_tests_schema

rango_test = Blueprint('rango_test', __name__)

# Crear un rango_test ----------------------------------------
@rango_test.route('/rango_test/v1', methods=['POST'])
def crear_rango_test():
    id_test = request.json.get("id_test")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    nuevo_rango_test = rango_test(id_test, minimo, maximo, diagnostico)
    db.session.add(nuevo_rango_test)
    db.session.commit()

    result = rango_test_schema.dump(nuevo_rango_test)
    return make_response(jsonify(result), 201)

# Listar todos los rango_tests ----------------------------------------
@rango_test.route('/rango_test/v1/listar', methods=['GET'])
def listar_rango_tests():
    all_rango_tests = Rango_test.query.all()
    result = rango_tests_schema.dump(all_rango_tests)

    return make_response(jsonify(result), 200)

# Obtener un rango_test por su ID ----------------------------------------
@rango_test.route('/rango_test/v1/<int:id>', methods=['GET'])
def obtener_rango_test(id):
    rango_test = Rango_test.query.get(id)

    if not rango_test:
        data = {
            'message': 'rango_test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = rango_test_schema.dump(rango_test)
    data = {
        'message': 'rango_test recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un rango_test por su ID ----------------------------------------
@rango_test.route('/rango_test/v1/<int:id>', methods=['PUT'])
def actualizar_rango_test(id):
    rango_test_actual = Rango_test.query.get(id)

    if not rango_test_actual:
        data = {
            'message': 'rango_test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_test = request.json.get("id_test")
    minimo = request.json.get("minimo")
    maximo = request.json.get("maximo")
    diagnostico = request.json.get("diagnostico")

    rango_test_actual.id_test = id_test
    rango_test_actual.minimo = minimo
    rango_test_actual.maximo = maximo
    rango_test_actual.diagnostico = diagnostico

    db.session.commit()

    result = rango_test_schema.dump(rango_test_actual)

    data = {
        'message': 'rango_test actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar un rango_test por su ID ----------------------------------------
@rango_test.route('/rango_test/v1/<int:id>', methods=['DELETE'])
def eliminar_rango_test(id):
    rango_test = Rango_test.query.get(id)

    if not rango_test:
        data = {
            'message': 'rango_test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(rango_test)
    db.session.commit()

    data = {
        'message': 'rango_test eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)

# Listar rango_tests por id_test ----------------------------------------
@rango_test.route('/rango_test/v1/test/<int:id_test>', methods=['GET'])
def listar_rango_tests_por_test(id_test):
    rango_tests = Rango_test.query.filter_by(id_test=id_test).all()

    result = rango_tests_schema.dump(rango_tests)

    if not rango_tests:
        data = {
            'message': 'No se encontraron rango_tests para el id_test proporcionado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'rango_tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)