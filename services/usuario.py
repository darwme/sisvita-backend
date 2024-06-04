from flask import Blueprint, request, jsonify, make_response
from model.usuario import Usuario
from utils.db import db
from schemas.usuario import usuario_schema, usuarios_schema

usuario_bp = Blueprint('usuario', __name__)  

# Crear un nuevo usuario
@usuario_bp.route('/usuario/v1', methods=['POST'])
def crear_usuario():

    # Extrae los datos del cuerpo de la solicitud
    nombre = request.json.get("nombre")
    apellido = request.json.get("apellido")
    email = request.json.get("email")
    clave = request.json.get("clave")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    tipo_usuario = request.json.get("tipo_usuario")
    is_admin = request.json.get("is_admin")

    nuevo_usuario = Usuario(nombre, apellido, email, clave, fecha_nacimiento, sexo, estado_civil, is_admin)
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    result = usuario_schema.dump(nuevo_usuario)

    data = {
        'message': 'Usuario creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los usuarios
@usuario_bp.route('/usuario/v1/listar', methods=['GET'])
def listar_usuarios():
    all_users = Usuario.query.all()
    result = usuarios_schema.dump(all_users)

    data = {
        'message': 'Usuarios recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener un usuario por su ID
@usuario_bp.route('/usuario/v1/<int:id>', methods=['GET'])
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

# Actualizar un usuario por su ID
@usuario_bp.route('/usuario/v1/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    nuevo_usuario = Usuario.query.get(id)

    if not nuevo_usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    nombre = request.json.get("nombre")
    apellido = request.json.get("apellido")
    email = request.json.get("email")
    clave = request.json.get("clave")
    fecha_nacimiento = request.json.get("fecha_nacimiento")
    sexo = request.json.get("sexo")
    estado_civil = request.json.get("estado_civil")
    is_admin = request.json.get("is_admin")

    nuevo_usuario.nombre = nombre
    nuevo_usuario.apellido = apellido
    nuevo_usuario.email = email
    nuevo_usuario.clave = clave
    nuevo_usuario.fecha_nacimiento = fecha_nacimiento
    nuevo_usuario.sexo = sexo
    nuevo_usuario.estado_civil = estado_civil
    nuevo_usuario.is_admin = is_admin

    db.session.commit()

    result = usuario_schema.dump(nuevo_usuario)

    data = {
        'message': 'Usuario actualizado correctamente',
        'status': 200,
        'data': result
    }   

    return make_response(jsonify(data), 200)

# Eliminar un usuario por su ID
@usuario_bp.route('/usuario/v1/<int:id>', methods=['DELETE'])
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