from flask import Blueprint, request, jsonify, make_response
from model.historial_test import Historial_test
from utils.db import db
from schemas.historial_test import historial_test_schema, historiales_tests_schema

historial_test = Blueprint('historial_test', __name__)

# Crear un historial de test ----------------------------------------
@historial_test.route('/historial_test/v1', methods=['POST'])
def crear_historial_test():
    id_usuario = request.json.get("id_usuario")
    id_test = request.json.get("id_test")
    fecha_realizada = request.json.get("fecha_realizada")
    puntajes = request.json.get("puntajes")
    diagnosticos = request.json.get("diagnosticos")

    nuevo_historial = Historial_test(id_usuario=id_usuario,id_test= id_test,
                                     fecha_realizada=fecha_realizada,
                                     puntajes=puntajes, diagnosticos=diagnosticos)
    db.session.add(nuevo_historial)
    db.session.commit()

    result = historial_test_schema.dump(nuevo_historial)

    data = {
        'message': 'Historial test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los historiales de test ----------------------------------------
@historial_test.route('/historial_test/v1/listar', methods=['GET'])
def listar_historiales_test():
    all_historiales = Historial_test.query.all()
    result = historiales_tests_schema.dump(all_historiales)

    data = {
        'message': 'Historiales de test recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener un historial de test por su ID ----------------------------------------
@historial_test.route('/historial_test/v1/<int:id>', methods=['GET'])
def obtener_historial_test(id):
    historial = Historial_test.query.get(id)

    if not historial:
        data = {
            'message': 'Historial de test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = historial_test_schema.dump(historial)
    data = {
        'message': 'Historial test recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un historial de test por su ID ----------------------------------------
@historial_test.route('/historial_test/v1/<int:id>', methods=['PUT'])
def actualizar_historial_test(id):
    historial_actual = Historial_test.query.get(id)

    if not historial_actual:
        data = {
            'message': 'Historial de test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_usuario = request.json.get("id_usuario")
    id_test = request.json.get("id_test")
    fecha_realizada = request.json.get("fecha_realizada")
    puntajes = request.json.get("puntajes")
    diagnosticos = request.json.get("diagnosticos")

    historial_actual.id_usuario = id_usuario
    historial_actual.id_test = id_test
    historial_actual.fecha_realizada = fecha_realizada
    historial_actual.puntajes = puntajes
    historial_actual.diagnosticos = diagnosticos

    db.session.commit()

    result = historial_test_schema.dump(historial_actual)

    data = {
        'message': 'Historial de test actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar un historial de test por su ID ----------------------------------------
@historial_test.route('/historial_test/v1/<int:id>', methods=['DELETE'])
def eliminar_historial_test(id):
    historial = Historial_test.query.get(id)

    if not historial:
        data = {
            'message': 'Historial test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(historial)
    db.session.commit()

    data = {
        'message': 'Historial test eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
