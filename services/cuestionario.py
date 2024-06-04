from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from model.cuestionario import Cuestionario
from utils.db import db
from schemas.cuestionario import cuestionario_schema, cuestionarios_schema

cuestionario= Blueprint('cuestionario', __name__)

@cuestionario.route('/cuestionario/v1', methods=['POST'])
@jwt_required()
def addCuestionario():
    id_cuestionario=request.json.get('id_cuestionario')
    id_test=request.json.get('id_test')
    id_seccion=request.json.get('id_seccion')
    total_cuestionario=request.json.get('total_cuestionario')

    nuevo_cuestionario=Cuestionario(id_cuestionario, id_test, id_seccion, total_cuestionario)
    db.session.add(nuevo_cuestionario)
    db.session.commit()

    result=cuestionario_schema.dump(nuevo_cuestionario)

    data={
        'message':'Cuestionario creado correctamente',
        'status':201,
        'data':result
    }

    return make_response(jsonify(data), 201)

@cuestionario.route('/cuestionario/v1/listar', methods=['GET'])
@jwt_required()
def getCuestionario():
    cuestionarios=Cuestionario.query.all()
    result=cuestionarios_schema.dump(cuestionarios)

    data={
        'message':'Cuestionarios recuperados correctamente',
        'status':200,
        'data':result
    }

    return make_response(jsonify(data), 200)

@cuestionario.route('/cuestionario/v1/<int:id>', methods=['GET'])
@jwt_required()
def getOne(id):
    cuestionario=Cuestionario.query.get(id)

    if not cuestionario:
        data={
            'message':'Cuestionario no encontrado',
            'status':404
        }

        return make_response(jsonify(data), 404)

    result=cuestionario_schema.dump(cuestionario)
    data={
        'message':'Cuestionario recuperado correctamente',
        'status':200,
        'data':result
    }

    return make_response(jsonify(data), 200)

@cuestionario.route('/cuestionario/v1/<int:id>', methods=['PUT'])
@jwt_required()
def updateOne(id):
    cuestionario = Cuestionario.query.get(id)

    if not cuestionario:
        data = {
            'message': 'Cuestionario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_cuestionario=request.json.get('id_cuestionario')
    id_test=request.json.get('id_test')
    id_seccion=request.json.get('id_seccion')
    total_cuestionario=request.json.get('total_cuestionario')

    cuestionario.id_cuestionario=id_cuestionario
    cuestionario.id_test=id_test
    cuestionario.id_seccion=id_seccion
    cuestionario.total_cuestionario=total_cuestionario

    db.session.commit()

    result=cuestionario_schema.dump(cuestionario)

    data={
        'message':'Cuestionario actualizado correctamente',
        'status':200,
        'data':result
    
    }

    return make_response(jsonify(data), 200)

@cuestionario.route('/cuestionario/v1/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteOne(id):
    cuestionario=Cuestionario.query.get(id)

    if not cuestionario:
        data={
            'message':'Cuestionario no encontrado',
            'status':404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(cuestionario)
    db.session.commit()

    data={
        'message':'Cuestionario eliminado correctamente',
        'status':200
    }

    return make_response(jsonify(data), 200)