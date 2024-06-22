from flask import Blueprint, request, jsonify ,make_response
from model.test import Test
from model.seccion import Seccion
from model.situacion import Situacion
from model.pregunta import Pregunta
from model.opcion import Opcion
from utils.db import db

from schemas.test import test_schema, tests_schema
from schemas.seccion import seccion_schema,secciones_schema
from schemas.situacion import situacion_schema,situaciones_schema
from schemas.pregunta import pregunta_schema,preguntas_schema
from schemas.opcion import opcion_schema,opciones_schema


def getSeccionesByIdTest(id_test):
    secciones = Seccion.query.filter_by(id_test=id_test).all()
    return secciones

def getSituacionesByIdSeccion(id_seccion):
    situaciones = Situacion.query.filter_by(id_seccion=id_seccion).all()
    return situaciones

def getPreguntasByIdSituacion(id_situacion):
    preguntas = Pregunta.query.filter_by(id_situacion=id_situacion).all()
    return preguntas

def getOpcionesByIdTest(id_test):
    opciones = Opcion.query.filter_by(id_test=id_test).all()
    return opciones

administrar = Blueprint('administrar', __name__)

@administrar.route('/administrar/v1/registrar/test', methods=['POST'])
def crear_test():
    try:
        data = request.json

        with db.session.begin():
            for test_name, test_data in data.items():
                # Crear nuevo test
                nuevo_test = Test(nombre=test_name)
                db.session.add(nuevo_test)
                db.session.flush()
                i = 0
                for opcion_data in test_data['opciones']:
                    # Crear nueva opcion
                    nueva_opcion = Opcion(id_test=nuevo_test.id_test, descripcion=opcion_data, valor_opcion=i)
                    i += 1
                    db.session.add(nueva_opcion)
                    db.session.flush()

                for seccion_name, seccion_data in test_data['secciones'].items():
                    # Crear nueva seccion
                    nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name)
                    db.session.add(nueva_seccion)
                    db.session.flush()

                    for situacion_data in seccion_data['situaciones']:
                        # Crear nueva situacion
                        nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'])
                        db.session.add(nueva_situacion)
                        db.session.flush()

                        for pregunta_texto in situacion_data['preguntas']:
                            # Crear nueva pregunta
                            nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_texto)
                            db.session.add(nueva_pregunta)
                            db.session.flush()

        return jsonify({'message': 'Datos cargados exitosamente', 'status': 201}), 201

    except Exception as e:
        print(e)
        db.session.rollback()
        print('rollback ejecutado...')
        return jsonify({'message': f'Error al cargar datos: {str(e)}', 'status': 500}), 500



@administrar.route('/administrar/v1/enviar/test', methods=['GET'])
def listar_tests_detalles():
    try:
        all_tests = Test.query.all()
        test_list = []
        for test in all_tests:
            opciones = getOpcionesByIdTest(test.id_test)
            secciones = getSeccionesByIdTest(test.id_test)
            test_data = test_schema.dump(test)
            test_data['opciones'] = opciones_schema.dump(opciones)
            print(test_data)
            test_data['secciones'] = []
            for seccion in secciones:
                situaciones = getSituacionesByIdSeccion(seccion.id_seccion)
                seccion_data = seccion_schema.dump(seccion)
                seccion_data['situaciones'] = []
                for situacion in situaciones:
                    preguntas = getPreguntasByIdSituacion(situacion.id_situacion)
                    situacion_data = situacion_schema.dump(situacion)
                    situacion_data['preguntas'] = []
                    for pregunta in preguntas:
                        pregunta_data = pregunta_schema.dump(pregunta)
                        print(pregunta_data)
                        situacion_data['preguntas'].append(pregunta_data)
                    seccion_data['situaciones'].append(situacion_data)
                test_data['secciones'].append(seccion_data)
            test_list.append(test_data)
        return jsonify(test_list)
    
    except Exception as e:
        print(e)
        return jsonify({'message': f'Error al listar los tests: {str(e)}', 'status': 500}), 500



