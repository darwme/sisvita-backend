# In service/cita_service.py
from flask import Blueprint, request, jsonify, make_response
from model.cita import Cita
from utils.db import db
from schemas.cita import cita_schema, citas_schema

# Define the Blueprint for 'cita'
cita = Blueprint('cita', __name__)

# Create a new cita ----------------------------------------
@cita.route('/cita/v1', methods=['POST'])
def crear_cita():
    id_especialista = request.json.get("id_especialista")
    id_paciente = request.json.get("id_paciente")
    fecha_agendada = request.json.get("fecha_agendada")
    estado = request.json.get("estado")
    motivo = request.json.get("motivo")
    hora = request.json.get("hora")

    nueva_cita = Cita(
        id_especialista=id_especialista, 
        id_paciente=id_paciente, 
        fecha_agendada=fecha_agendada, 
        estado=estado, 
        motivo=motivo,
        hora=hora
    )
    
    db.session.add(nueva_cita)
    db.session.commit()

    result = cita_schema.dump(nueva_cita)

    data = {
        'message': 'Cita creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# List all citas ----------------------------------------
@cita.route('/cita/v1/listar', methods=['GET'])
def listar_citas():
    all_citas = Cita.query.all()
    result = citas_schema.dump(all_citas)

    data = {
        'message': 'Citas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Get a cita by ID ----------------------------------------
@cita.route('/cita/v1/<int:id>', methods=['GET'])
def obtener_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = cita_schema.dump(cita)
    data = {
        'message': 'Cita recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Update a cita by ID ----------------------------------------
@cita.route('/cita/v1/<int:id>', methods=['PUT'])
def actualizar_cita(id):
    cita_existente = Cita.query.get(id)

    if not cita_existente:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_especialista = request.json.get("id_especialista")
    id_paciente = request.json.get("id_paciente")
    fecha_agendada = request.json.get("fecha_agendada")
    estado = request.json.get("estado")
    motivo = request.json.get("motivo")
    hora = request.json.get("hora")

    cita_existente.id_especialista = id_especialista
    cita_existente.id_paciente = id_paciente
    cita_existente.fecha_agendada = fecha_agendada
    cita_existente.estado = estado
    cita_existente.motivo = motivo
    cita_existente.hora = hora

    db.session.commit()

    result = cita_schema.dump(cita_existente)

    data = {
        'message': 'Cita actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Delete a cita by ID ----------------------------------------
@cita.route('/cita/v1/<int:id>', methods=['DELETE'])
def eliminar_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(cita)
    db.session.commit()

    data = {
        'message': 'Cita eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
