# In service/paciente_service.py
from flask import Blueprint, request, jsonify, make_response
from model.paciente import Paciente
from utils.db import db
from schemas.paciente import paciente_schema, pacientes_schema

# Define the Blueprint for 'paciente'
paciente = Blueprint('paciente', __name__)

# Create a new paciente ----------------------------------------
@paciente.route('/paciente/v1', methods=['POST'])
def crear_paciente():
    id_persona = request.json.get("id_persona")
    codigo_paciente = request.json.get("codigo_paciente")
    antecedentes = request.json.get("antecedentes")

    nuevo_paciente = Paciente(
        id_persona=id_persona, 
        codigo_paciente=codigo_paciente, 
        antecedentes=antecedentes
    )
    
    db.session.add(nuevo_paciente)
    db.session.commit()

    result = paciente_schema.dump(nuevo_paciente)

    data = {
        'message': 'Paciente creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# List all pacientes ----------------------------------------
@paciente.route('/paciente/v1/listar', methods=['GET'])
def listar_pacientes():
    all_pacientes = Paciente.query.all()
    result = pacientes_schema.dump(all_pacientes)

    data = {
        'message': 'Pacientes recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Get a paciente by ID ----------------------------------------
@paciente.route('/paciente/v1/<int:id>', methods=['GET'])
def obtener_paciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = paciente_schema.dump(paciente)
    data = {
        'message': 'Paciente recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Update a paciente by ID ----------------------------------------
@paciente.route('/paciente/v1/<int:id>', methods=['PUT'])
def actualizar_paciente(id):
    paciente_existente = Paciente.query.get(id)

    if not paciente_existente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_persona = request.json.get("id_persona")
    codigo_paciente = request.json.get("codigo_paciente")
    antecedentes = request.json.get("antecedentes")

    paciente_existente.id_persona = id_persona
    paciente_existente.codigo_paciente = codigo_paciente
    paciente_existente.antecedentes = antecedentes

    db.session.commit()

    result = paciente_schema.dump(paciente_existente)

    data = {
        'message': 'Paciente actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Delete a paciente by ID ----------------------------------------
@paciente.route('/paciente/v1/<int:id>', methods=['DELETE'])
def eliminar_paciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(paciente)
    db.session.commit()

    data = {
        'message': 'Paciente eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
