# In service/usuario_service.py
from flask import Blueprint, request, jsonify, make_response
from model.usuario import Usuario
from utils.db import db
from schemas.usuario import usuario_schema, usuarios_schema

# Define the Blueprint for 'usuario'
usuario = Blueprint('usuario', __name__)

# Create a new usuario ----------------------------------------
@usuario.route('/usuario/v1', methods=['POST'])
def crear_usuario():
    email = request.json.get("email")
    clave = request.json.get("clave")
    print("aqui")
    nuevo_usuario = Usuario(email,clave)
    db.session.add(nuevo_usuario)
    db.session.commit()
    print("aqui2")
    result = usuario_schema.dump(nuevo_usuario)

    data = {
        'message': 'Usuario creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# List all usuarios ----------------------------------------
@usuario.route('/usuario/v1/listar', methods=['GET'])
def listar_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)

    data = {
        'message': 'Usuarios recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Get a usuario by ID ----------------------------------------
@usuario.route('/usuario/v1/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = usuario_schema.dump(usuario)
    data = {
        'message': 'Usuario recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Update a usuario by ID ----------------------------------------
@usuario.route('/usuario/v1/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario_existente = Usuario.query.get(id)

    if not usuario_existente:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    email = request.json.get("email")
    clave = request.json.get("clave")

    usuario_existente.email = email
    usuario_existente.clave = clave

    db.session.commit()

    result = usuario_schema.dump(usuario_existente)

    data = {
        'message': 'Usuario actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Delete a usuario by ID ----------------------------------------
@usuario.route('/usuario/v1/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(usuario)
    db.session.commit()

    data = {
        'message': 'Usuario eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)
