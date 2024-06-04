from flask import Blueprint, request, jsonify, make_response
from model.usuario import Usuario
from model.estudiante import Estudiante
from utils.db import db
from schemas.usuario import usuario_schema, usuarios_schema
from schemas.estudiante import estudiante_schema, estudiantes_schema
from schemas.especialista import especialista_schema, especialistas_schema

auth = Blueprint('auth', __name__)

@auth.route('/auth/v1/estudiante/register', methods=['POST'])
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
        carrera_profesional = request.json.get("carrera_profesional")

        nuevo_usuario = Usuario(nombre, apellido, email, clave, fecha_nacimiento, sexo, estado_civil, is_admin)
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        result1 = usuario_schema.dump(nuevo_usuario)

        iduser = nuevo_usuario.id_usuario
        if not iduser:
            raise Exception('Error al registrar el usuario')

        nuevo_estudiante = Estudiante(iduser, codigo_estudiante, carrera_profesional)

        db.session.add(nuevo_estudiante)
        db.session.commit()

        result2 = estudiante_schema.dump(nuevo_estudiante)

        result = {**result1, **result2}

        data = {
            'message': 'Usuario Alumno registrado correctamente',
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
    
@auth.route('/auth/v1/estudiante/login', methods=['POST'])
def login():
    try:
        email = request.json.get("email")
        clave = request.json.get("clave")
        print("email: ", email, "clave: ", clave)
        usuario = Usuario.query.filter_by(email=email, clave=clave).first()
        print("usuario: ", usuario)

        if not usuario:
            raise Exception('Usuario no encontrado')
        print("usuario id: ", usuario.id_usuario)
        estudiante = Estudiante.query.filter_by(id_usuario=usuario.id_usuario).first()

        if not estudiante:
            raise Exception('Estudiante no encontrado')

        result1 = usuario_schema.dump(usuario)
        result2 = estudiante_schema.dump(estudiante)

        result = {**result1, **result2}

        data = {
            'message': 'Usuario Alumno logueado correctamente',
            'status': 200,
            'data': result
        }

        return jsonify(data), 200

    except Exception as e:
        error_data = {
            'message': 'Error al loguear el usuario estudiante',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500


