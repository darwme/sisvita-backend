# In service/administrador_service.py
from flask import Blueprint, request, jsonify, make_response
from model.administrador import Administrador
from utils.db import db
from schemas.administrador import administrador_schema, administradores_schema

# Define the Blueprint for 'administrador'
administrador = Blueprint('administrador', __name__)

# Create a new administrador ----------------------------------------
@administrador.route('/administrador/v1', methods=['POST'])
def crear_administrador():
    id_usuario = request.json.get("id_usuario")
    nombre_admin = request.json.get("nombre_admin")

    nuevo_administrador = Administrador(id_usuario=id_usuario, nombre_admin=nombre_admin)
    db.session.add(nuevo_administrador)
    db.session.commit()

    result = administrador_schema.dump(nuevo_administrador)

    data = {
        'message': 'Administrador creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# List all administradores ----------------------------------------
@administrador.route('/administrador/v1/listar', methods=['GET'])
def listar_administradores():
    all_administradores = Administrador.query.all()
    result = administradores_schema.dump(all_administradores)

    data = {
        'message': 'Administradores recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Get an administrador by ID ----------------------------------------
@administrador.route('/administrador/v1/<int:id>', methods=['GET'])
def obtener_administrador(id):
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

# Update an administrador by ID ----------------------------------------
@administrador.route('/administrador/v1/<int:id>', methods=['PUT'])
def actualizar_administrador(id):
    administrador_existente = Administrador.query.get(id)

    if not administrador_existente:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_usuario = request.json.get("id_usuario")
    nombre_admin = request.json.get("nombre_admin")

    administrador_existente.id_usuario = id_usuario
    administrador_existente.nombre_admin = nombre_admin

    db.session.commit()

    result = administrador_schema.dump(administrador_existente)

    data = {
        'message': 'Administrador actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Delete an administrador by ID ----------------------------------------
@administrador.route('/administrador/v1/<int:id>', methods=['DELETE'])
def eliminar_administrador(id):
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
