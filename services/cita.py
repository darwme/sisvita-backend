from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db
from model.cita import Cita
from schemas.cita import cita_schema, citas_schema

cita_blueprint = Blueprint('cita', __name__)

@cita_blueprint.route('/cita/v1', methods=['POST'])
@jwt_required()
def addCita():
    id_especialista = request.json.get("id_especialista")
    id_paciente = request.json.get("id_paciente")
    fecha_agenda = request.json.get("fecha_agenda")
    estado = request.json.get("estado")
    motivo = request.json.get("motivo")

    nueva_cita = Cita(id_especialista=id_especialista, id_paciente=id_paciente,
                      fecha_agenda=fecha_agenda, estado=estado, motivo=motivo)
    db.session.add(nueva_cita)
    db.session.commit()

    result = cita_schema.dump(nueva_cita)

    data = {
        'message': 'Cita creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@cita_blueprint.route('/cita/v1/listar', methods=['GET'])
@jwt_required()
def getCitas():
    citas = Cita.query.all()
    result = citas_schema.dump(citas)

    data = {
        'message': 'Citas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@cita_blueprint.route('/cita/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOneCita(id):
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

@cita_blueprint.route('/cita/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOneCita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_especialista = request.json.get("id_especialista")
    id_paciente = request.json.get("id_paciente")
    fecha_agenda = request.json.get("fecha_agenda")
    estado = request.json.get("estado")
    motivo = request.json.get("motivo")

    cita.id_especialista = id_especialista
    cita.id_paciente = id_paciente
    cita.fecha_agenda = fecha_agenda
    cita.estado = estado
    cita.motivo = motivo

    db.session.commit()

    result = cita_schema.dump(cita)

    data = {
        'message': 'Cita actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@cita_blueprint.route('/cita/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOneCita(id):
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


