from flask import Blueprint, request, jsonify, make_response
from model.ubicacion import Ubicacion
from utils.db import db
from schemas.ubicacion import ubicacion_schema, ubicaciones_schema


ubicacion = Blueprint('ubicacion', __name__)

#Obtener todas las ubicaciones
@ubicacion.route('/ubicaciones/v1', methods=['GET'])
def get_ubicaciones():
    ubicaciones = Ubicacion.query.all()

    if not ubicaciones:
        return jsonify({'message': 'No hay ubicaciones'})
    
    return jsonify(ubicaciones_schema.dump(ubicaciones))


#Obtener una ubicacion
@ubicacion.route('/ubicacion/v1/<int:id_ubicacion>', methods=['GET'])
def get_ubicacion(id_ubicacion):
    ubicacion = Ubicacion.query.get(id_ubicacion)

    if not ubicacion:
        return jsonify({'message': 'No se encontro la ubicacion'})
    
    return jsonify(ubicacion_schema.dump(ubicacion))
