from flask import Blueprint, request, jsonify, make_response
from model.ubicacion import Ubicacion
from utils.db import db
from schemas.ubicacion import ubicacion_schema, ubicaciones_schema
from typing import List

class Distrito:
    def __init__(self, nombre: str, ubigeo: str, y: float, x: float):
        self.nombre = nombre
        self.ubigeo = ubigeo
        self.y = y
        self.x = x
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "ubigeo": self.ubigeo,
            "y": self.y,
            "x": self.x
        }

class Provincia:
    def __init__(self, nombre: str, distritos: List[Distrito] = None):
        self.nombre = nombre
        if distritos is None:
            self.distritos = []
        else:
            self.distritos = distritos

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "distritos": [distrito.to_dict() for distrito in self.distritos]
        }



gestor_ubicacion = Blueprint('gestor_ubicacion', __name__)

#Obtener todas las ubicaciones
@gestor_ubicacion.route('/ubicaciones/v1', methods=['GET'])
def get_ubicaciones():
    ubicaciones = Ubicacion.query.all()

    provincias_dict = {}
    
    for row in ubicaciones:
        distrito = Distrito(row.distrito, row.ubigeo, row.y, row.x)
        if row.provincia not in provincias_dict:
            provincias_dict[row.provincia] = Provincia(row.provincia, [distrito])
        else:
            provincias_dict[row.provincia].distritos.append(distrito)
    
    provincias = [provincia.to_dict() for provincia in provincias_dict.values()]
    
    return jsonify(provincias)




#Obtener una ubicacion
@gestor_ubicacion.route('/gestor_ubicacion/v1/<int:id_ubicacion>', methods=['GET'])
def get_ubicacion(id_ubicacion):
    ubicacion = Ubicacion.query.get(id_ubicacion)

    if not ubicacion:
        return jsonify({'message': 'No se encontro la ubicacion'})
    
    return jsonify(ubicacion_schema.dump(ubicacion))
