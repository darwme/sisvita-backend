from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db
from model.administrador import Administrador
from schemas.administrador import administrador_schema, administradores_schema

administrador_blueprint = Blueprint('administrador', __name__)

@administrador_blueprint.route('/administrador/v1', methods=['POST'])
@jwt_required()
def addAdministrador():
    id_usuario = request.json.get("id_usuario")
    nombre_admin = request.json.get("nombre_admin")

    nuevo_administrador = Administrador(id_usuario,nombre_admin)
    db.session.add(nuevo_administrador)
    db.session.commit()

    result = administrador_schema.dump(nuevo_administrador)

    data = {
        'message': 'Administrador creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@administrador_blueprint.route('/administrador/v1/listar', methods=['GET'])
@jwt_required()
def getAdministradores():
    administradores = Administrador.query.all()
    result = administradores_schema.dump(administradores)

    data = {
        'message': 'Administradores recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_blueprint.route('/administrador/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOneAdministrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    result = administrador_schema.dump(administrador)
    data = {
        'message': 'Administrador recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_blueprint.route('/administrador/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOneAdministrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_usuario = request.json.get("id_usuario")
    nombre_admin = request.json.get("nombre_admin")

    administrador.id_usuario = id_usuario
    administrador.nombre_admin = nombre_admin

    db.session.commit()

    result = administrador_schema.dump(administrador)

    data = {
        'message': 'Administrador actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_blueprint.route('/administrador/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOneAdministrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(administrador)
    db.session.commit()

    data = {
        'message': 'Administrador eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
