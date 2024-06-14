from flask import Blueprint, request, jsonify, make_response
from model.clasificacion import Clasificacion
from utils.db import db
from schemas.clasificacion import clasificacion_schema, clasificaciones_schema

clasificacion = Blueprint('clasificacion', __name__)

# Crear una clasificacion  ----------------------------------------
@clasificacion.route('/clasificacion/v1', methods=['POST'])
def crear_clasificacion():
    id_clasificacion = request.json.get("id_clasificacion")
    nombre = request.json.get("nombre")

    nueva_clasificacion = Clasificacion(id_clasificacion, nombre)
    db.session.add(nueva_clasificacion)
    db.session.commit()

    result = clasificacion_schema.dump(nueva_clasificacion)

    data = {
        'message': 'Clasificacion creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las clasificaicones ----------------------------------------
@clasificacion.route('/clasificacion/v1/listar', methods=['GET'])
def listar_clasificiones():
    all_clasificaciones = Clasificacion.query.all()
    result = clasificaciones_schema.dump(all_clasificaciones)

    data = {
        'message': 'Clasificaciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una clasificacion por su ID ----------------------------------------
@clasificacion.route('/clasificacion/v1/<int:id>', methods=['GET'])
def obtener_clasificacion(id):
    clasificacion = Clasificacion.query.get(id)

    if not clasificacion:
        data = {
            'message': 'Clasificacion no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = clasificacion_schema.dump(clasificacion)
    data = {
        'message': 'Clasificacion recuperada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una Clasificacion por su ID ----------------------------------------
@clasificacion.route('/clasificacion/v1/<int:id>', methods=['PUT'])
def actualizar_clasificacion(id):
    nueva_clasificacion = Clasificacion.query.get(id)

    if not nueva_clasificacion:
        data = {
            'message': 'Clasificacion no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    id_clasificacion = request.json.get("id_clasificacion")
    nombre = request.json.get("nombre")

    nueva_clasificacion.id_clasificacion = id_clasificacion
    nueva_clasificacion.nombre = nombre

    db.session.commit()

    result = clasificacion_schema.dump(nueva_clasificacion)

    data = {
        'message': 'Clasificacion actualizada correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Eliminar una clasificacion por su ID ----------------------------------------
@clasificacion.route('/clasificacion/v1/<int:id>', methods=['DELETE'])
def eliminar_clasificacion(id):
    clasificacion = Clasificacion.query.get(id)

    if not clasificacion:
        data = {
            'message': 'Clasificacion no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(clasificacion)
    db.session.commit()

    data = {
        'message': 'Clasificacion eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)