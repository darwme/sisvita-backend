from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.diagnostico import Diagnostico
from utils.db import db
from schemas.diagnostico import DiagnosticoSchema

diagnostico = Blueprint('diagnostico', __name__)

@diagnostico.route('/diagnostico/v1', methods=['POST'])
@jwt_required()
def add_diagnostico():
    id_diagnostico=request.json.get('id_diagnostico')
    id_test = request.json.get('id_test')
    id_clasificacion = request.json.get('id_clasificacion')
    categoria = request.json.get('categoria')
    puntaje = request.json.get('puntaje')

    nuevo_diagnostico = Diagnostico(id_diagnostico,id_test,id_clasificacion,categoria,puntaje)
    db.session.add(nuevo_diagnostico)
    db.session.commit()

    diagnostico_schema = DiagnosticoSchema()
    result = diagnostico_schema.dump(nuevo_diagnostico)

    data = {
        'message': 'Diagnóstico creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@diagnostico.route('/diagnostico/<int:id>', methods=['GET'])
@jwt_required()
def get_diagnostico(id):
    diagnostico = Diagnostico.query.get(id)

    if not diagnostico:
        data = {
            'message': 'Diagnóstico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    diagnostico_schema = DiagnosticoSchema()
    result = diagnostico_schema.dump(diagnostico)

    data = {
        'message': 'Diagnóstico recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@diagnostico.route('/diagnostico', methods=['GET'])
@jwt_required()
def get_diagnosticos():
    diagnosticos = Diagnostico.query.all()

    diagnosticos_schema = DiagnosticoSchema(many=True)
    result = diagnosticos_schema.dump(diagnosticos)

    data = {
        'message': 'Diagnosticos recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@diagnostico.route('/diagnostico/<int:id>', methods=['PUT'])
@jwt_required()
def update_diagnostico(id):
    diagnostico = Diagnostico.query.get(id)

    if not diagnostico:
        data = {
            'message': 'Diagnóstico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    diagnostico.id_diagnostico = request.json.get('id_diagnostico')
    diagnostico.id_test = request.json.get('id_test')
    diagnostico.id_clasificacion = request.json.get('id_clasificacion')
    diagnostico.categoria = request.json.get('categoria')
    diagnostico.puntaje = request.json.get('puntaje')

    db.session.commit()

    diagnostico_schema = DiagnosticoSchema()
    result = diagnostico_schema.dump(diagnostico)

    data = {
        'message': 'Diagnóstico actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@diagnostico.route('/diagnostico/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_diagnostico(id):
    diagnostico = Diagnostico.query.get(id)

    if not diagnostico:
        data = {
            'message': 'Diagnóstico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(diagnostico)
    db.session.commit()

    data = {
        'message': 'Diagnóstico eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
