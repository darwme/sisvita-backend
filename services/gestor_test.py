from flask import Blueprint, request, jsonify ,make_response
from model.test import Test
from model.seccion import Seccion
from model.situacion import Situacion
from model.pregunta import Pregunta
from model.opcion import Opcion
from model.rango_seccion import Rango_seccion
from model.rango_test import Rango_test
from model.historial_test import Historial_test
from utils.db import db

from schemas.test import test_schema, tests_schema
from schemas.seccion import seccion_schema,secciones_schema
from schemas.situacion import situacion_schema,situaciones_schema
from schemas.pregunta import pregunta_schema,preguntas_schema
from schemas.opcion import opcion_schema,opciones_schema
from schemas.rango_seccion import rango_seccion_schema,rango_secciones_schema
from schemas.rango_test import rango_test_schema,rango_tests_schema


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

gestor_test = Blueprint('gestor_test', __name__)

@gestor_test.route('/gestor_test/v1/administrador/registrar_test', methods=['POST'])
def crear_test():
    try:
        data = request.json
        
        # Extraer el nombre y la descripción del test ISRA
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')

        with db.session.begin():
            # Crear el test ISRA
            nuevo_test = Test(nombre=nombre, descripcion=descripcion)
            db.session.add(nuevo_test)
            db.session.flush()

            # Procesar las secciones del test ISRA
            if 'secciones' in data:
                secciones_data = data['secciones']
                for seccion_name, seccion_data in secciones_data.items():
                    nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name)
                    db.session.add(nueva_seccion)
                    db.session.flush()

                    if 'situaciones' in seccion_data:
                        for situacion_data in seccion_data['situaciones']:
                            nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'])
                            db.session.add(nueva_situacion)
                            db.session.flush()

                            if 'preguntas' in situacion_data:
                                for pregunta_texto in situacion_data['preguntas']:
                                    nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_texto)
                                    db.session.add(nueva_pregunta)
                                    db.session.flush()

                    if 'rango_seccion' in seccion_data:
                        for rango_data in seccion_data['rango_seccion']:
                            nueva_rango_seccion = Rango_seccion(id_seccion=nueva_seccion.id_seccion, minimo=rango_data['minimo'], maximo=rango_data['maximo'], diagnostico=rango_data['diagnostico'])
                            db.session.add(nueva_rango_seccion)
                            db.session.flush()

            # Procesar el rango de test ISRA
            if 'rango_test' in data:
                for rango_data in data['rango_test']:
                    nuevo_rango_test = Rango_test(id_test=nuevo_test.id_test, minimo=rango_data['minimo'], maximo=rango_data['maximo'], diagnostico=rango_data['diagnostico'])
                    db.session.add(nuevo_rango_test)
                    db.session.flush()

            # Procesar las opciones del test ISRA
            if 'opciones' in data:
                for opcion_data in data['opciones']:
                    nueva_opcion = Opcion(id_test=nuevo_test.id_test, descripcion=opcion_data['descripcion'], valor_opcion=opcion_data['valor_opcion'])
                    db.session.add(nueva_opcion)
                    db.session.flush()
                    
        result = test_schema.dump(nuevo_test)

        data = {
            'message': 'Test registrado correctamente',
            'status': 201,
            'data': result
        }

        return jsonify(data), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al cargar datos: {str(e)}', 'status': 500}), 500



@gestor_test.route('/gestor_test/v1/listar_tests', methods=['GET'])
def listar_tests_detalles():
    try:
        all_tests = Test.query.all()
        test_list = []
        for test in all_tests:
            opciones = getOpcionesByIdTest(test.id_test)
            secciones = getSeccionesByIdTest(test.id_test)
            test_data = test_schema.dump(test)
            test_data['opciones'] = opciones_schema.dump(opciones)
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
                        pregunta_data['id_pregunta'] = pregunta.id_pregunta 
                        #print('id_pregunta', pregunta_data['id_pregunta'])
                        #print(pregunta_data)
                        situacion_data['preguntas'].append(pregunta_data)
                    seccion_data['situaciones'].append(situacion_data)
                test_data['secciones'].append(seccion_data)
            test_list.append(test_data)
        return jsonify(test_list)
    
    except Exception as e:
        #print(e)
        return jsonify({'message': f'Error al listar los tests: {str(e)}', 'status': 500}), 500



@gestor_test.route('/gestor_test/v1/administrador/eliminar_test/<int:id_test>', methods=['DELETE'])
def eliminar_test_completo(id_test):
    try:
        # Buscar el test por su ID
        test = Test.query.get(id_test)

        if not test:
            return jsonify({'message': 'Test no encontrado', 'status': 404}), 404

        # Eliminar registros de historial_test asociados al test
        historiales_test = Historial_test.query.filter_by(id_test=id_test).all()
        for historial_test in historiales_test:
            db.session.delete(historial_test)
            
        # Eliminar opciones asociadas al test
        opciones = Opcion.query.filter_by(id_test=id_test).all()
        for opcion in opciones:
            db.session.delete(opcion)

        # Eliminar rangos de test asociados al test
        rangos_test = Rango_test.query.filter_by(id_test=id_test).all()
        for rango_test in rangos_test:
            db.session.delete(rango_test)

        # Eliminar secciones asociadas al test
        secciones = Seccion.query.filter_by(id_test=id_test).all()
        for seccion in secciones:
            # Eliminar rangos de seccion asociados a cada seccion
            rangos_seccion = Rango_seccion.query.filter_by(id_seccion=seccion.id_seccion).all()
            for rango_seccion in rangos_seccion:
                db.session.delete(rango_seccion)

            # Eliminar situaciones asociadas a cada seccion
            situaciones = Situacion.query.filter_by(id_seccion=seccion.id_seccion).all()
            for situacion in situaciones:
                # Eliminar preguntas asociadas a cada situacion
                preguntas = Pregunta.query.filter_by(id_situacion=situacion.id_situacion).all()
                for pregunta in preguntas:
                    db.session.delete(pregunta)
                db.session.delete(situacion)

            db.session.delete(seccion)



        # Finalmente, eliminar el test
        db.session.delete(test)
        
        db.session.commit()  # Commit la transacción una vez todas las operaciones de eliminación han terminado

        return jsonify({'message': 'Test y todas sus relaciones eliminados correctamente', 'status': 200}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al eliminar el test y sus relaciones: {str(e)}', 'status': 500}), 500
