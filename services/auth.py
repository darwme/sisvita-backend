from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token
from model.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from model.estudiante import Estudiante
from model.especialista import Especialista
from utils.db import db
from schemas.usuario import usuario_schema, usuarios_schema
from schemas.estudiante import estudiante_schema, estudiantes_schema
from schemas.especialista import especialista_schema, especialistas_schema

auth = Blueprint('auth', __name__)

@auth.route('/auth/v1/register', methods=['POST'])
def register():
    try:
        nombre = request.json.get("nombre")
        apellido = request.json.get("apellido")
        email = request.json.get("email")
        clave = request.json.get("clave")
        fecha_nacimiento = request.json.get("fecha_nacimiento")
        sexo = request.json.get("sexo")
        estado_civil = request.json.get("estado_civil")
        is_admin = request.json.get("is_admin")
        codigo_estudiante = request.json.get("codigo_estudiante")
        tipo_usuario = request.json.get("tipo_usuario")
        carrera_profesional = request.json.get("carrera_profesional")
        especialidad = request.json.get("especialidad")

        clave_hash = generate_password_hash(clave)
        nuevo_usuario = Usuario(nombre, apellido, email, clave_hash, fecha_nacimiento, sexo, estado_civil, tipo_usuario, is_admin)
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        result1 = usuario_schema.dump(nuevo_usuario)
        
        iduser = nuevo_usuario.id_usuario
        if not iduser:
            raise Exception('Error al registrar el usuario')
        
        result2 = {}
        tipo = nuevo_usuario.tipo_usuario.lower()
        if tipo == 'estudiante':
            nuevo_estudiante = Estudiante(iduser, codigo_estudiante, carrera_profesional)
            db.session.add(nuevo_estudiante)
            db.session.commit()

            result2 = estudiante_schema.dump(nuevo_estudiante)
        if tipo == 'especialista':
            nuevo_especialista = Especialista(iduser, especialidad)
            db.session.add(nuevo_especialista)
            db.session.commit()

            result2 = especialista_schema.dump(nuevo_especialista)


        result = {**result1, **result2}

        data = {
            'message': 'Se registró correctamente',
            'status': 201,
            'data': result
        }

        return jsonify(data), 201

    except Exception as e:
        # En caso de error, hacer rollback a la sesión y mostrar un mensaje de error
        db.session.rollback()
        error_data = {
            'message': 'Error al registrar el usuario estudiante',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
    
@auth.route('/auth/v1/login', methods=['POST'])
def login():
    try:
        email = request.json.get("email")
        clave = request.json.get("clave")
        tipo_usuario = request.json.get("tipo_usuario")

        print("email: ", email, "clave: ", clave, "tipo_usuario: ", tipo_usuario)

        usuario = Usuario.query.filter_by(email=email).first()
        token = None
        result3 = {}
        if usuario and check_password_hash(usuario.clave, clave):

            token = create_access_token(identity=usuario.id_usuario)
            result3 = {'token': token}
        else:
            raise Exception('Usuario no encontrado')
        
        result1 = usuario_schema.dump(usuario)
        result2 = {}
        tipo = usuario.tipo_usuario.lower()

        if tipo == 'estudiante':
            estudiante = Estudiante.query.filter_by(id_usuario=usuario.id_usuario).first()
            result2 = estudiante_schema.dump(estudiante)

            if not estudiante:
                raise Exception('Estudiante no encontrado')
        
        if tipo == 'especialista':
            especialista = Especialista.query.filter_by(id_usuario=usuario.id_usuario).first()
            result2 = especialista_schema.dump(especialista)

            if not especialista:
                raise Exception('Especialista no encontrado')

        result = {**result3, **result1, **result2}

        data = {
            'message': 'Usuario Alumno logueado correctamente',
            'status': 200,
            'data': result
        }

        return jsonify(data), 200

    except Exception as e:
        error_data = {
            'message': 'Error al loguear el usuario',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500


