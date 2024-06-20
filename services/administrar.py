from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.situacion import Situacion
from model.pregunta import Pregunta
from model.opcion import Opcion
from utils.db import db

administrar = Blueprint('administrar', __name__)

@administrar.route('/administrar/v1/registrar/test', methods=['POST'])
def crear_test():
    try:
        data = request.json

        # Recorrer cada test en el JSON
        for test_name, test_data in data.items():
            # Crear nuevo test
            nuevo_test = Test(nombre=test_name)
            db.session.add(nuevo_test)
            db.session.commit()

            cant_secciones = 0  # Contador de secciones en el test

            # Recorrer cada seccion en el test
            for seccion_name, seccion_data in test_data['secciones'].items():
                # Crear nueva seccion
                nueva_seccion = Seccion(id_test=nuevo_test.id_test, descripcion=seccion_name, cant_situaciones=0, cant_opciones=0)
                db.session.add(nueva_seccion)
                db.session.commit()

                cant_situaciones = 0  # Contador de situaciones en la seccion

                # Recorrer cada situacion en la seccion
                for situacion_data in seccion_data['situaciones']:
                    # Crear nueva situacion
                    nueva_situacion = Situacion(id_seccion=nueva_seccion.id_seccion, descripcion=situacion_data['situacion'], cant_preguntas=0)
                    db.session.add(nueva_situacion)
                    db.session.commit()

                    cant_preguntas = 0  # Contador de preguntas en la situacion

                    # Recorrer cada pregunta en la situacion
                    for pregunta_texto in situacion_data['preguntas']:
                        # Crear nueva pregunta
                        nueva_pregunta = Pregunta(id_situacion=nueva_situacion.id_situacion, descripcion=pregunta_texto)
                        db.session.add(nueva_pregunta)
                        db.session.commit()
                        cant_preguntas += 1

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

            # Registrar opciones si existen para el test
            if 'opciones' in test_data:
                opciones = test_data['opciones']
                for opcion_texto in opciones:
                    nueva_opcion = Opcion(id_test=nuevo_test.id_test, descripcion=opcion_texto)
                    db.session.add(nueva_opcion)
                    db.session.commit()

                # Actualizar cantidad de opciones en el test (aunque este valor no se guarda en la base de datos en este caso)
                nuevo_test.cant_opciones = len(opciones)
                db.session.commit()

        return jsonify({'message': 'Datos cargados exitosamente', 'status': 201}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al cargar datos: {str(e)}', 'status': 500}), 500
