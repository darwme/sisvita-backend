# In service/especialista_service.py
from flask import Blueprint, request, jsonify, make_response
from model.especialista import Especialista
from utils.db import db
from schemas.especialista import especialista_schema, especialistas_schema

# Define the Blueprint for 'especialista'
especialista = Blueprint('especialista', __name__)

# Create a new especialista ----------------------------------------
@especialista.route('/especialista/v1', methods=['POST'])
def crear_especialista():
    data = request.get_json()
    id_persona = data.get("id_persona")
    codigo_especialista = data.get("codigo_especialista")
    especialista = data.get("especialista")
    experiencia = data.get("experiencia")

    nuevo_especialista = Especialista(
        id_persona=id_persona,
        codigo_especialista=codigo_especialista,
        especialista=especialista,
        experiencia=experiencia
    )
    db.session.add(nuevo_especialista)
    db.session.commit()

    result = especialista_schema.dump(nuevo_especialista)

    response_data = {
        'message': 'Especialista creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(response_data), 201)

# List all especialistas ----------------------------------------
@especialista.route('/especialista/v1/listar', methods=['GET'])
def listar_especialistas():
    all_especialistas = Especialista.query.all()
    result = especialistas_schema.dump(all_especialistas)

    response_data = {
        'message': 'Especialistas recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(response_data), 200)

# Get an especialista by ID ----------------------------------------
@especialista.route('/especialista/v1/<int:id>', methods=['GET'])
def obtener_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        response_data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(response_data), 404)
    
    result = especialista_schema.dump(especialista)
    response_data = {
        'message': 'Especialista recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(response_data), 200)

# Update an especialista by ID ----------------------------------------
@especialista.route('/especialista/v1/<int:id>', methods=['PUT'])
def actualizar_especialista(id):
    especialista_existente = Especialista.query.get(id)

    if not especialista_existente:
        response_data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(response_data), 404)

    data = request.get_json()
    id_persona = data.get("id_persona")
    codigo_especialista = data.get("codigo_especialista")
    especialista = data.get("especialista")
    experiencia = data.get("experiencia")

    especialista_existente.id_persona = id_persona
    especialista_existente.codigo_especialista = codigo_especialista
    especialista_existente.especialista = especialista
    especialista_existente.experiencia = experiencia

    db.session.commit()

    result = especialista_schema.dump(especialista_existente)

    response_data = {
        'message': 'Especialista actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(response_data), 200)

# Delete an especialista by ID ----------------------------------------
@especialista.route('/especialista/v1/<int:id>', methods=['DELETE'])
def eliminar_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        response_data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(response_data), 404)

    db.session.delete(especialista)
    db.session.commit()

    response_data = {
        'message': 'Especialista eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(response_data), 200)
