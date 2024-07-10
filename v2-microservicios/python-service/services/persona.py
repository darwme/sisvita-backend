# In service/persona_service.py
from flask import Blueprint, request, jsonify, make_response
from model.persona import Persona
from utils.db import db
from schemas.persona import persona_schema, personas_schema

# Define the Blueprint for 'persona'
persona = Blueprint('persona', __name__)

# Create a new persona ----------------------------------------
@persona.route('/persona/v1', methods=['POST'])
def crear_persona():
    id_usuario = request.json.get("id_usuario")
    nombres = request.json.get("nombres")
    apellidos = request.json.get("apellidos")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    celular = request.json.get("celular")

    nueva_persona = Persona(
        id_usuario=id_usuario, 
        nombres=nombres, 
        apellidos=apellidos, 
        sexo=sexo, 
        estado_civil=estado_civil, 
        fecha_nacimiento=fecha_nacimiento, 
        celular=celular
    )
    
    db.session.add(nueva_persona)
    db.session.commit()

    result = persona_schema.dump(nueva_persona)

    data = {
        'message': 'Persona creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# List all personas ----------------------------------------
@persona.route('/persona/v1/listar', methods=['GET'])
def listar_personas():
    all_personas = Persona.query.all()
    result = personas_schema.dump(all_personas)

    data = {
        'message': 'Personas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Get a persona by ID ----------------------------------------
@persona.route('/persona/v1/<int:id>', methods=['GET'])
def obtener_persona(id):
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

# Update a persona by ID ----------------------------------------
@persona.route('/persona/v1/<int:id>', methods=['PUT'])
def actualizar_persona(id):
    persona_existente = Persona.query.get(id)

    if not persona_existente:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_usuario = request.json.get("id_usuario")
    nombres = request.json.get("nombres")
    apellidos = request.json.get("apellidos")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    celular = request.json.get("celular")

    persona_existente.id_usuario = id_usuario
    persona_existente.nombres = nombres
    persona_existente.apellidos = apellidos
    persona_existente.sexo = sexo
    persona_existente.fecha_nacimiento = fecha_nacimiento
    persona_existente.sexo = sexo
    persona_existente.estado_civil = estado_civil
    persona_existente.celular = celular

    db.session.commit()

    result = persona_schema.dump(persona_existente)

    data = {
        'message': 'Persona actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Delete a persona by ID ----------------------------------------
@persona.route('/persona/v1/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
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
