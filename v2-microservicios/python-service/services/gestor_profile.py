import json
from flask import Blueprint, request, jsonify, make_response
from model.especialista import Especialista
from model.paciente import Paciente
from schemas.gestion_profile import especialista_profile_schema, paciente_profile_schema
from utils.db import db
from datetime import datetime


gestor_profile = Blueprint('gestor_profile', __name__)

@gestor_profile.route('/gestor_profile/v1/especialista/<cod_especialista>', methods=['GET'])
def informacionEspecialista(cod_especialista):
    try:
        # Obtener el especialista por su código
        especialista = Especialista.query.filter_by(codigo_especialista=cod_especialista).first()

        if not especialista:
            return jsonify({'message': f'No se encontró especialista con código {cod_especialista}', 'status': 404}), 404

        especialista_data = especialista_profile_schema.dump(especialista)

        return jsonify(especialista_data), 200

    except Exception as e:
        return jsonify({'message': f'Error al obtener información del especialista: {str(e)}', 'status': 500}), 500


@gestor_profile.route('/gestor_profile/v1/paciente/<cod_paciente>', methods=['GET'])
def informacionPaciente(cod_paciente):
    try:
        # Obtener el paciente por su código
        paciente = Paciente.query.filter_by(codigo_paciente=cod_paciente).first()

        if not paciente:
            return jsonify({'message': f'No se encontró paciente con código {cod_paciente}', 'status': 404}), 404

        # Serializar los datos del paciente usando el esquema PacienteProfileSchema
        paciente_data = paciente_profile_schema.dump(paciente)

        return jsonify(paciente_data), 200

    except Exception as e:
        return jsonify({'message': f'Error al obtener información del paciente: {str(e)}', 'status': 500}), 500
    
    


@gestor_profile.route('/gestor_profile/v1/especialista/update/<cod_especialista>', methods=['PUT'])
def actualizarEspecialista(cod_especialista):
    try:
        # Obtener el especialista por su código
        especialista = Especialista.query.filter_by(codigo_especialista=cod_especialista).first()

        if not especialista:
            return jsonify({'message': f'No se encontró especialista con código {cod_especialista}', 'status': 404}), 404

        # Obtener datos de la solicitud
        data = request.json

        # Actualizar los campos del especialista
        especialista.especialidad = data['especialidad']
        especialista.experiencia = data['experiencia']

        # Actualizar los campos de la persona asociada
        persona_data = data['persona']
        persona = especialista.persona

        persona.nombres = persona_data['nombres']
        persona.apellidos = persona_data['apellidos']
        persona.fecha_nacimiento = persona_data['fecha_nacimiento']
        persona.sexo = persona_data['sexo']
        persona.estado_civil = persona_data['estado_civil']
        persona.celular = persona_data['celular']

        # Confirmar todos los cambios en la base de datos
        db.session.commit()
        especialista_actualizado = especialista_profile_schema.dump(especialista)
        return jsonify(especialista_actualizado), 200

    except Exception as e:
        db.session.rollback()  # Manejar la excepción y revertir los cambios
        return jsonify({'message': f'Error al actualizar el especialista: {str(e)}', 'status': 500}), 500

    
    

@gestor_profile.route('/gestor_profile/v1/paciente/update/<cod_paciente>', methods=['PUT'])
def actualizarPaciente(cod_paciente):
    try:
        data = request.json

        # Obtener el paciente por su código
        paciente = Paciente.query.filter_by(codigo_paciente=cod_paciente).first()

        if not paciente:
            return jsonify({'message': f'No se encontró paciente con código {cod_paciente}', 'status': 404}), 404

        # Actualizar los datos del paciente
        paciente.antecedentes = data.get('antecedentes', paciente.antecedentes)

        # Actualizar los datos de la persona asociada al paciente
        persona = paciente.persona
        persona.nombres = data['persona'].get('nombres', persona.nombres)
        persona.apellidos = data['persona'].get('apellidos', persona.apellidos)
        persona.fecha_nacimiento = data['persona'].get('fecha_nacimiento', persona.fecha_nacimiento)
        persona.sexo = data['persona'].get('sexo', persona.sexo)
        persona.estado_civil = data['persona'].get('estado_civil', persona.estado_civil)
        persona.celular = data['persona'].get('celular', persona.celular)

        # Guardar los cambios en la base de datos
        db.session.commit()

        # Actualizar el esquema del paciente y devolver la respuesta
        paciente_actualizado = paciente_profile_schema.dump(paciente)
        return jsonify(paciente_actualizado), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al actualizar el paciente: {str(e)}', 'status': 500}), 500