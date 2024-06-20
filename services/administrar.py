from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.situacion import Situacion
from model.pregunta import Pregunta
from utils.db import db
from schemas.test import tests_schema
from schemas.seccion import seccionSchema
from schemas.situacion import situacionSchema
from schemas.pregunta import preguntaSchema

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

            cant_secciones = 0

            for seccion_name, seccion_data in test_data['secciones'].items():
                # Crear nueva seccion
                nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name)
                db.session.add(nueva_seccion)
                db.session.commit()

                cant_situaciones = 0

                for situacion_data in seccion_data['situaciones']:
                    # Crear nueva situacion
                    nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'])
                    db.session.add(nueva_situacion)
                    db.session.commit()

                    cant_preguntas = len(situacion_data['preguntas'])

                    for pregunta_data in situacion_data['preguntas']:
                        # Crear nueva pregunta
                        nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_data)
                        db.session.add(nueva_pregunta)
                        db.session.commit()

                    # Actualizar cantidad de preguntas en la situacion
                    nueva_situacion.cant_preguntas = cant_preguntas
                    db.session.commit()

                    cant_situaciones += 1

                # Actualizar cantidad de situaciones en la seccion
                nueva_seccion.cant_situaciones = cant_situaciones
                db.session.commit()

                cant_secciones += 1

            # Actualizar cantidad de secciones en el test
            nuevo_test.cant_secciones = cant_secciones
            db.session.commit()

        return jsonify({'message': 'Datos cargados exitosamente'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al cargar datos: {str(e)}'}), 500
