from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.especialista import Especialista
from utils.db import db
from schemas.especialista import especialista_schema, especialistas_schema

especialista= Blueprint('especialista', __name__)

@especialista.route('/especialidad/v1', methods=['POST'])
@jwt_required()
def addEspecialista():
    id_especialista = request.json.get("id_especialista")
    id_usuario = request.json.get("id_usuario")
    especialidad = request.json.get("especialidad")
    
    nuevo_especialista = Especialista(id_especialista, id_usuario, especialidad)
    db.session.add(nuevo_especialista)
    db.session.commit()
    
    result = especialista_schema.dump(nuevo_especialista)
    
    data = {
        'message': 'Especialista creado correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@especialista.route('/especialista/v1/listar', methods=['GET'])
@jwt_required()
def getEspecialista():
    especialistas = Especialista.query.all()
    result = especialistas_schema.dump(especialistas)
    
    data = {
        'message': 'Especialistas recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOne(id):
    especialista = Especialista.query.get(id)
    
    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    result = especialista_schema.dump(especialista)
    data = {
        'message': 'Especialista recuperado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOne(id):

    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_especialista = request.json.get("id_especialista")
    id_usuario = request.json.get("id_usuario")
    especialidad = request.json.get("especialidad")

    especialista.id_especialista = id_especialista
    especialista.id_usuario = id_usuario
    especialista.especialidad = especialidad

    db.session.commit()

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOne(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(especialista)
    db.session.commit()

    data = {
        'message': 'Especialista eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)