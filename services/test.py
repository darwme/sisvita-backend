from flask import Blueprint, request, jsonify, make_response
from model.test import Test
from utils.db import db
from schemas.test import test_schema, tests_schema

# Define el Blueprint del 'test'
test = Blueprint('test', __name__)

# Crear un test ----------------------------------------
@test.route('/test/v1', methods=['POST'])
def crear_test():
    nombre = request.json.get("nombre")

    nuevo_test = Test(nombre)
    db.session.add(nuevo_test)
    db.session.commit()

    result = test_schema.dump(nuevo_test)

    data = {
        'message': 'Test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los tests ----------------------------------------
@test.route('/test/v1/listar', methods=['GET'])
def listar_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener un test por su ID ----------------------------------------
@test.route('/test/v1/<int:id>', methods=['GET'])
def obtener_test(id):
    test = Test.query.get(id)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = test_schema.dump(test)
    data = {
        'message': 'Test recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un test por su ID ----------------------------------------
@test.route('/test/v1/<int:id>', methods=['PUT'])
def actualizar_test(id):
    nuevo_test = Test.query.get(id)

    if not nuevo_test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_test = request.json.get("id_test")
    nombre = request.json.get("nombre")
    
    nuevo_test.id_test = id_test
    nuevo_test.nombre = nombre
    
    db.session.commit()

    result = test_schema.dump(nuevo_test)

    data = {
        'message': 'Test actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar un test por su ID ----------------------------------------
@test.route('/test/v1/<int:id>', methods=['DELETE'])
def eliminar_test(id):
    test = Test.query.get(id)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(test)
    db.session.commit()

    data = {
        'message': 'Test eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
