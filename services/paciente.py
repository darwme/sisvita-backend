from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.paciente import Paciente  
from schemas.paciente import paciente_schema, pacientes_schema  

paciente = Blueprint('paciente', __name__)

@paciente.route('/paciente/listar/v1', methods=['POST'])
def addPaciente():
   
    id_persona=request.json.get("id_persona")
    codigo_paciente = request.json.get("codigo_paciente")
    antecedentes = request.json.get("antecedentes")
    

    nuevo_paciente = Paciente(id_persona,codigo_paciente, antecedentes)
    db.session.add(nuevo_paciente)
    db.session.commit()

    result = paciente_schema.dump(nuevo_paciente)

    data = {
        'message': 'Paciente creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)


@paciente.route('/paciente//', methods=['GET'])
def getPacientes():
    pacientes = Paciente.query.all()
    result = pacientes_schema.dump(pacientes)

    data = {
        'message': 'Pacientes recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


@paciente.route('/paciente/v1/<int:id>', methods=['GET'])
def getOnePaciente(id):
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


@paciente.route('/paciente/v1/', methods=['PUT'])
def updateOnePaciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_persona = request.json.get("id_persona")
    codigo_paciente = request.json.get("codigo_paciente")
    antecedentes = request.json.get("antecedentes")
   

    id_persona.id_persona = id_persona
    paciente.codigo_paciente = codigo_paciente
    paciente.antecendentes = antecedentes

    db.session.commit()

    result = paciente_schema.dump(paciente)

    data = {
        'message': 'Paciente actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


@paciente.route('/paciente/v1/', methods=['DELETE'])
def deleteOnePaciente(id):
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
