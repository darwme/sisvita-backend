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


administrar = Blueprint('administrar', __name__)

@administrar.route('/administrar/v1/registrar/test', methods=['POST'])
def crear_test():
    try:
        data = request.json

        for test_name, test_data in data.items():
            # Crear nuevo test
            nuevo_test = Test(nombre=test_name)
            db.session.add(nuevo_test)
            db.session.commit()

            for seccion_name, seccion_data in test_data['secciones'].items():
                # Crear nueva seccion
                nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name)
                db.session.add(nueva_seccion)
                db.session.commit()

                for situacion_data in seccion_data['situaciones']:
                    # Crear nueva situacion
                    nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'])
                    db.session.add(nueva_situacion)
                    db.session.commit()

                    for pregunta_texto in situacion_data['preguntas']:
                        # Crear nueva pregunta
                        nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_texto)
                        db.session.add(nueva_pregunta)
                        db.session.commit()

                # Registrar opciones si existen para la seccion
                if 'opciones' in test_data and seccion_name in test_data['opciones']:
                    opciones = test_data['opciones'][seccion_name]
                    for opcion_texto in opciones:
                        nueva_opcion = Opcion(id_seccion=nueva_seccion.id_seccion, descripcion=opcion_texto)
                        db.session.add(nueva_opcion)
                        db.session.commit()

        return jsonify({'message': 'Datos cargados exitosamente', 'status': 201}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al cargar datos: {str(e)}', 'status': 500}), 500








#--------------------
#
@administrar.route('/administrar/v1/enviar/test', methods=['GET'])
def listar_tests_detalles():
    all_tests = Test.query.all()
    test_list = []
    for test in all_tests:
        secciones = listar_secciones_por_test(test.id_test)
        test_info = {
            'nombre': test.nombre,
            'secciones': secciones
        }
        test_list.append(test_info)
    
    # Retornar el JSON directamente
    return jsonify({
        'data': test_list
    })
#secciones
def listar_secciones_por_test(id_test):
    
    secciones = Seccion.query.filter_by(id_test=id_test).all()
    
    secciones_list = []
    for sec in secciones:
        situaciones = listar_situaciones_por_seccion(sec.id_seccion)
        seccion_info = {
            'descripcion': sec.descripcion,
            'situaciones': situaciones
        }
        secciones_list.append(seccion_info)
    
    return jsonify({
        'data': secciones_list
    })
#situaciones   
def listar_situaciones_por_seccion(id_seccion):
    
    situaciones = Situacion.query.filter_by(id_seccion=id_seccion).all()
    
    situaciones_list = []
    for sit in situaciones:
        preguntas = listar_preguntas_por_situacion(sit.id_situacion)
        situacion_info = {
            'descripcion': sit.descripcion,
            'situaciones': preguntas
        }
        situaciones_list.append(situacion_info)
    
    return jsonify({
        'data': situaciones_list
    })

#preguntas
def listar_preguntas_por_situacion(id_situacion):
    
    situaciones = Pregunta.query.filter_by(id_situacion=id_situacion).all()
    
    preguntas_list = []
    for preg in situaciones:
        pregunta_info = {
            'descripcion': preg.descripcion
        }
        preguntas_list.append(pregunta_info)
    
    return jsonify({
        'data': preguntas_list
    })

