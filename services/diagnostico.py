from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.diagnostico import Diagnostico
from utils.db import db
from schemas.diagnostico import diagnostico_schema, diagnosticos_schema

diagnostico = Blueprint('diagnostico', __name__)  # Crea un blueprint llamado 'diagnostico'

# Crear un nuevo diagnostico -----------------------------------------
@diagnostico.route('/diagnostico/v1', methods=['POST'])
@jwt_required()
def crear_diagnostico():
    id_test = request.json.get("id_test")
    categoria = request.json.get("categoria")
    puntaje = request.json.get("puntaje")
    id_clasificacion = request.json.get("id_clasificacion")
    
    nuevo_diagnostico = Diagnostico(id_test,categoria,puntaje,id_clasificacion)
    db.session.add(nuevo_diagnostico)
    db.session.commit()

    result = diagnostico_schema.dump(nuevo_diagnostico)

    data = {
        'message': 'Diagnostico creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)


# Listar todos los diagnosticos -----------------------------------------
@diagnostico.route('/diagnostico/v1/listar', methods=['GET'])
@jwt_required()
def listar_diagnosticos():
    all_diagnosticos = Diagnostico.query.all()
    result = diagnosticos_schema.dump(all_diagnosticos)

    data = {
        'message': 'Diagnosticos recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


# Obtener un Diagnostico por su ID -----------------------------------------
@diagnostico.route('/diagnostico/v1/<int:id>', methods=['GET'])
@jwt_required()
def obtener_diagnostico(id):
    diagnostico = Diagnostico.query.get(id)

    if not diagnostico:
        data = {
            'message': 'Diagnostico no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = diagnostico_schema.dump(diagnostico)

    data = {
        'message': 'Diagnostico recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un diagnostico por su ID -----------------------------------------
@diagnostico.route('/diagnostico/v1/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_diagnostico(id):
    nuevo_diagnostico = Diagnostico.query.get(id)

    if not nuevo_diagnostico:
        data = {
            'message': 'Diagnostico no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_diagnostico = request.json.get("id_diagnostico")
    id_test = request.json.get("id_test")
    categoria = request.json.get("categoria")
    puntaje = request.json.get("puntaje")
    id_clasificacion = request.json.get('id_clasificacion')
    
    nuevo_diagnostico.id_diagnostico = id_diagnostico
    nuevo_diagnostico.id_test = id_test
    nuevo_diagnostico.id_categoria = categoria
    nuevo_diagnostico.id_puntaje = puntaje
    nuevo_diagnostico.id_clasificacion = id_clasificacion

    db.session.commit()

    result = diagnosticos_schema.dump(nuevo_diagnostico)

    data = {
        'message': 'diagnostico actualizado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)


# Eliminar un test por su ID -------------------------------------------
@diagnostico.route('/diagnostico/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_diagnostico(id):

    viejo_diagnostico = Diagnostico.query.get(id)

    if not viejo_diagnostico:
        data = {
            'message': 'Diagnostico no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(viejo_diagnostico)
    db.session.commit()

    data = {
        'message': 'diagnostico eliminado correctamente',
        'status': 202
    }

    return make_response(jsonify(data), 202)