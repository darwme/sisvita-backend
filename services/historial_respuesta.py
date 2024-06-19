from flask import Blueprint, request, jsonify, make_response
from model.historial_respuesta import Historial_respuesta
from utils.db import db
from schemas.historial_respuesta import Historial_respuesta_schema, Historiales_respuestas_schema

historial_respuesta = Blueprint('historial_respuesta', __name__)

# Crear una entrada en historial_respuesta
@historial_respuesta.route('/historial_respuesta/v1', methods=['POST'])
def crear_historial_respuesta():
    id_historial_test = request.json.get("id_historial_test")
    id_respuesta = request.json.get("id_respuesta")
    
    nueva_historial_respuesta = Historial_respuesta(id_historial_test,id_respuesta)
    
    db.session.add(nueva_historial_respuesta)
    db.session.commit()
    
    result = Historial_respuesta_schema().dump(nueva_historial_respuesta)
    
    data = {
        'message': 'Historial de respuesta creado correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

# Listar todas las entradas de historial_respuesta
@historial_respuesta.route('/historial_respuesta/v1/listar', methods=['GET'])
def listar_historiales_respuestas():
    historiales_respuestas = Historial_respuesta.query.all()
    result = Historiales_respuestas_schema.dump(historiales_respuestas)
    
    data = {
        'message': 'Historiales de respuestas recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

# Obtener una entrada específica por su ID
@historial_respuesta.route('/historial_respuesta/v1/<int:id>', methods=['GET'])
def obtener_historial_respuesta(id):
    historial_respuesta = Historial_respuesta.query.get(id)
    
    if not historial_respuesta:
        data = {
            'message': 'Historial de respuesta no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    result = Historial_respuesta_schema().dump(historial_respuesta)
    
    data = {
        'message': 'Historial de respuesta recuperado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

# Actualizar una entrada existente por su ID
@historial_respuesta.route('/historial_respuesta/v1/<int:id>', methods=['PUT'])
def actualizar_historial_respuesta(id):
    historial_respuesta = Historial_respuesta.query.get(id)
    
    if not historial_respuesta:
        data = {
            'message': 'Historial de respuesta no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    id_historial_test = request.json.get("id_historial_test")
    id_respuesta = request.json.get("id_respuesta")
    
    historial_respuesta.id_historial_test = id_historial_test
    historial_respuesta.id_respuesta = id_respuesta
    
    db.session.commit()
    
    result = Historial_respuesta_schema().dump(historial_respuesta)
    
    data = {
        'message': 'Historial de respuesta actualizado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

# Eliminar una entrada por su ID
@historial_respuesta.route('/historial_respuesta/v1/<int:id>', methods=['DELETE'])
def eliminar_historial_respuesta(id):
    historial_respuesta = Historial_respuesta.query.get(id)
    
    if not historial_respuesta:
        data = {
            'message': 'Historial de respuesta no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(historial_respuesta)
    db.session.commit()
    
    data = {
        'message': 'Historial de respuesta eliminado correctamente',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)
