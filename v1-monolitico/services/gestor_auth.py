from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from model.usuario import Usuario
from model.administrador import Administrador
from model.persona import Persona
from model.paciente import Paciente
from model.especialista import Especialista
from model.ubicacion import Ubicacion

from utils.db import db

from schemas.usuario import usuario_schema, usuarios_schema
from schemas.administrador import administrador_schema, administradores_schema
from schemas.persona import persona_schema, personas_schema
from schemas.paciente import paciente_schema, pacientes_schema
from schemas.especialista import especialista_schema, especialistas_schema
from schemas.ubicacion import ubicacion_schema,ubicaciones_schema

import secrets
import string

gestor_auth = Blueprint('gestor_auth', __name__)

def crear_usuario_y_persona(datos, tipo_persona):
    try:
        email = datos.get("email")
        clave = datos.get("clave")
        tipo_usuario = datos.get("tipo_usuario")

        clave_hash = generate_password_hash(clave)

        if tipo_usuario == 'administrador':
            raise ValueError('No se puede registrar un administrador desde esta ruta')

        if not tipo_usuario:
            tipo_usuario = Usuario.__table__.c.tipo_usuario.default.arg

        nuevo_usuario = Usuario(email, clave_hash,tipo_usuario)
        db.session.add(nuevo_usuario)
        db.session.commit()

        id_usuario = nuevo_usuario.id_usuario
        if not id_usuario:
            raise Exception('Error al registrar el usuario')

        # Validación de ubigeo
        ubigeo = datos.get("ubigeo")
        ubicacion = Ubicacion.query.filter_by(ubigeo=ubigeo).first()
        if not ubicacion:
            raise ValueError('El ubigeo proporcionado no es válido')
        
        nueva_persona = Persona(
            ubigeo=ubigeo,
            id_usuario=id_usuario,
            nombres=datos.get("nombres"),
            apellidos=datos.get("apellidos"),
            fecha_nacimiento=datos.get("fecha_nacimiento"),
            sexo=datos.get("sexo"),
            estado_civil=datos.get("estado_civil"),
            celular=datos.get("celular"),
            tipo_persona=tipo_persona
        )
        db.session.add(nueva_persona)
        db.session.commit()

        if not nueva_persona.id_persona:
            raise Exception('Error al registrar la persona')

        return nueva_persona

    except Exception as e:
        db.session.rollback()
        raise e

def generar_codigo_aleatorio(longitud=8):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return codigo


@gestor_auth.route('/gestor_auth/v1/register/paciente', methods=['POST'])
def registrar_paciente():
    try:
        datos = request.json
        tipo_persona1 = 'paciente'
        if not datos.get("email") or not datos.get("clave"):
            raise ValueError("El email y la clave son campos obligatorios")

        
        # Validación de campos específicos para paciente
        #if not datos.get("codigo_paciente"):
        #    raise ValueError("El código de paciente es un campo obligatorio")
        codigo_paciente = generar_codigo_aleatorio()
        
        # Crear usuario y persona
        nueva_persona = crear_usuario_y_persona(datos, tipo_persona1)
        
        # Crear paciente
        nuevo_paciente = Paciente(
            id_persona=nueva_persona.id_persona,
            codigo_paciente=codigo_paciente,
            antecedentes=datos.get("antecedentes")
        )
        db.session.add(nuevo_paciente)
        db.session.commit()
        
        result = paciente_schema.dump(nuevo_paciente)

        data = {
            'message': 'Paciente registrado correctamente',
            'status': 201,
            'data': result
        }

        return jsonify(data), 201

    except ValueError as ve:
        error_data = {
            'message': str(ve),
            'status': 400
        }
        return jsonify(error_data), 400

    except Exception as e:
        db.session.rollback()
        error_data = {
            'message': 'Error al registrar el paciente',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500

@gestor_auth.route('/gestor_auth/v1/register/especialista', methods=['POST'])
def registrar_especialista():
    try:
        datos = request.json
        tipo_persona1 = 'especialista'
        # Validación de campos específicos para especialista
        codigo_especialista = generar_codigo_aleatorio()
        
        # Crear usuario y persona
        nueva_persona = crear_usuario_y_persona(datos, tipo_persona1)

        # Crear especialista
        nuevo_especialista = Especialista(
            id_persona=nueva_persona.id_persona,
            codigo_especialista=codigo_especialista,
            especialidad=datos.get("especialidad"),
            experiencia=datos.get("experiencia")
        )
        db.session.add(nuevo_especialista)
        db.session.commit()
        
        result = especialista_schema.dump(nuevo_especialista)

        data = {
            'message': 'Especialista registrado correctamente',
            'status': 201,
            'data': result
        }

        return jsonify(data), 201

    except ValueError as ve:
        error_data = {
            'message': str(ve),
            'status': 400
        }
        return jsonify(error_data), 400

    except Exception as e:
        db.session.rollback()
        error_data = {
            'message': 'Error al registrar el especialista',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500

  
@gestor_auth.route('/gestor_auth/v1/login', methods=['POST'])
def login():
    try:
        email = request.json.get("email")
        clave = request.json.get("clave")
        
        # Buscar al usuario por su email
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.clave, clave):
            # Crear token de acceso
            token = create_access_token(identity=usuario.id_usuario)

            # Inicializar resultado
            result = {
                'token': token,
                'usuario': usuario_schema.dump(usuario)
            }
            
            # Comprobar si es un paciente
            paciente = Paciente.query.filter_by(id_persona=usuario.id_usuario).first()
            if paciente:
                result['paciente'] = paciente_schema.dump(paciente)

            # Comprobar si es un especialista
            especialista = Especialista.query.filter_by(id_persona=usuario.id_usuario).first()
            if especialista:
                result['especialista'] = especialista_schema.dump(especialista)

            data = {
                'message': 'Usuario logueado correctamente',
                'status': 200,
                'data': result
            }

            return jsonify(data), 200
        else:
            # Autenticación fallida
            return jsonify({
                'message': 'Credenciales incorrectas',
                'status': 401
            }), 401

    except Exception as e:

        error_data = {
            'message': 'Error al procesar el login',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
