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
