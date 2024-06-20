from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.situacion import Situacion
from model.pregunta import Pregunta
from model.opcion import Opcion
from utils.db import db
from schemas.test import test_schema
from schemas.seccion import seccion_schema
from schemas.situacion import situacionSchema
from schemas.pregunta import preguntaSchema
from schemas.opcion import opcion_schema

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
            result = test_schema.dump(nuevo_test)
            
            data = {
                'message': 'Test registrado correctamente',
                'status': 201,
                'data': result
            }

            cant_secciones = 0

            for seccion_name, seccion_data in test_data['secciones'].items():
                # Crear nueva seccion
                nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name)
                db.session.add(nueva_seccion)
                db.session.commit()
                
                result2 = test_schema.dump(nueva_seccion)
                data = {
                    'message': 'seccion registrada correctamente',
                    'status': 201,
                    'data': result2
                }

                cant_situaciones = 0

                for situacion_data in seccion_data['situaciones']:
                    # Crear nueva situacion
                    nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'])
                    db.session.add(nueva_situacion)
                    db.session.commit()

                    result3 = test_schema.dump(nueva_situacion)
                    data = {
                        'message': 'situacion registrada correctamente',
                        'status': 201,
                        'data': result3
                    }
                    cant_preguntas = len(situacion_data['preguntas'])

                    for pregunta_data in situacion_data['preguntas']:
                        # Crear nueva pregunta
                        nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_data)
                        db.session.add(nueva_pregunta)
                        db.session.commit()

                        result3 = test_schema.dump(nueva_situacion)
                        data = {
                            'message': 'situacion registrada correctamente',
                            'status': 201,
                            'data': result3
                        }

                # Actualizar cantidad de preguntas en la seccion
                nueva_situacion.cant_preguntas = cant_preguntas
                db.session.commit()

                cant_situaciones += 1

                # Verificar si hay opciones para crear
                if 'opciones' in test_data and seccion_name in test_data['opciones']:
                    opciones = test_data['opciones'][seccion_name]
                    for opcion_texto in opciones:
                        nueva_opcion = Opcion(id_test=nuevo_test.id_test, descripcion=opcion_texto, valor_opcion=0)
                        db.session.add(nueva_opcion)
                        db.session.commit()

                    # Actualizar cantidad de opciones en la seccion
                    nueva_seccion.cant_opciones = len(opciones)
                    db.session.commit()

                cant_secciones += 1

            # Actualizar cantidad de situaciones en la seccion
            nueva_seccion.cant_situaciones = cant_situaciones
            db.session.commit()

            # Actualizar cantidad de secciones en el test
            nuevo_test.cant_secciones = cant_secciones
            db.session.commit()

        return jsonify({'message': 'Datos cargados exitosamente'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al cargar datos: {str(e)}'}), 500
