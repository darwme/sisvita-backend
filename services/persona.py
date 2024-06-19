from flask import Flask, Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db
from model.persona import Persona
from schemas.persona import persona_schema, personas_schema

persona_blueprint = Blueprint('persona', __name__)

@persona_blueprint.route('/persona/v1', methods=['POST'])
@jwt_required()
def addPersona():
    id_usuario = request.json.get("id_usuario")
    nombres = request.json.get("nombres")
    apellidos = request.json.get("apellidos")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    
    nueva_persona = Persona(id_usuario, nombres, apellidos,sexo, estado_civil, fecha_nacimiento)
    db.session.add(nueva_persona)
    db.session.commit()
    
    result = persona_schema.dump(nueva_persona)
    
    data = {
        'message': 'Persona creada correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@persona_blueprint.route('/persona/v1/listar', methods=['GET'])
@jwt_required()
def getPersonas():
    personas = Persona.query.all()
    result = personas_schema.dump(personas)
    
    data = {
        'message': 'Personas recuperadas correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@persona_blueprint.route('/persona/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOnePersona(id):
    persona = Persona.query.get(id)
    
    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    result = persona_schema.dump(persona)
    data = {
        'message': 'Persona recuperada correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@persona_blueprint.route('/persona/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOnePersona(id):
    persona = Persona.query.get(id)
    
    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    id_usuario = request.json.get("id_usuario")
    nombres = request.json.get("nombres")
    apellidos = request.json.get("apellidos")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    
    persona.id_usuario = id_usuario
    persona.nombres = nombres
    persona.apellidos = apellidos
    persona.sexo = sexo
    persona.estado_civil = estado_civil
    persona.fecha_nacimiento = fecha_nacimiento
    
    db.session.commit()
    
    result = persona_schema.dump(persona)
    
    data = {
        'message': 'Persona actualizada correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@persona_blueprint.route('/persona/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOnePersona(id):
    persona = Persona.query.get(id)
    
    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(persona)
    db.session.commit()
    
    data = {
        'message': 'Persona eliminada correctamente',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)

