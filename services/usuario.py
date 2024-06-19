from flask import Flask, Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db
from model.usuario import Usuario
from schemas.usuario import usuario_schema, usuarios_schema

usuario_blueprint = Blueprint('usuario', __name__)

@usuario_blueprint.route('/usuario/v1', methods=['POST'])
@jwt_required()
def addUsuario():
    clave = request.json.get("clave")
    email = request.json.get("email")
    
    nuevo_usuario = Usuario(clave, email)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    result = usuario_schema.dump(nuevo_usuario)
    
    data = {
        'message': 'Usuario creado correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@usuario_blueprint.route('/usuario/v1/listar', methods=['GET'])
@jwt_required()
def getUsuarios():
    usuarios = Usuario.query.all()
    result = usuarios_schema.dump(usuarios)
    
    data = {
        'message': 'Usuarios recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@usuario_blueprint.route('/usuario/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOneUsuario(id):
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

@usuario_blueprint.route('/usuario/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOneUsuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    clave = request.json.get("clave")
    email = request.json.get("email")
    
    usuario.clave = clave
    usuario.email = email
    
    db.session.commit()
    
    result = usuario_schema.dump(usuario)
    
    data = {
        'message': 'Usuario actualizado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@usuario_blueprint.route('/usuario/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOneUsuario(id):
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

