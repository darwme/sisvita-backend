from flask import Flask, Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db
from model.especialista import Especialista
from schemas.especialista import especialista_schema, especialistas_schema

especialista_blueprint = Blueprint('especialista', __name__)

@especialista_blueprint.route('/especialista/v1', methods=['POST'])
@jwt_required()
def addEspecialista():
    id_persona = request.json.get("id_persona")
    codigo_especialista = request.json.get("codigo_especialista")
    especialidad = request.json.get("especialidad")
    experiencia = request.json.get("experiencia")
    
    nuevo_especialista = Especialista(id_persona, codigo_especialista,especialidad, experiencia)
    db.session.add(nuevo_especialista)
    db.session.commit()
    
    result = especialista_schema.dump(nuevo_especialista)
    
    data = {
        'message': 'Especialista creado correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@especialista_blueprint.route('/especialista/v1/listar', methods=['GET'])
@jwt_required()
def getEspecialistas():
    especialistas = Especialista.query.all()
    result = especialistas_schema.dump(especialistas)
    
    data = {
        'message': 'Especialistas recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@especialista_blueprint.route('/especialista/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOneEspecialista(id):
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

@especialista_blueprint.route('/especialista/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOneEspecialista(id):
    especialista = Especialista.query.get(id)
    
    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    id_persona = request.json.get("id_persona")
    codigo_especialista = request.json.get("codigo_especialista")
    especialidad = request.json.get("especialidad")
    experiencia = request.json.get("experiencia")
    
    especialista.id_persona = id_persona
    especialista.codigo_especialista = codigo_especialista
    especialista.especialidad = especialidad
    especialista.experiencia = experiencia
    
    db.session.commit()
    
    result = especialista_schema.dump(especialista)
    
    data = {
        'message': 'Especialista actualizado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@especialista_blueprint.route('/especialista/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOneEspecialista(id):
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

