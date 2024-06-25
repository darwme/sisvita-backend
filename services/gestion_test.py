from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.seccion_respuesta import Seccion_respuesta
from model.usuario import Usuario
from model.rango_seccion import Rango_seccion
from model.rango_test import Rango_test
from model.historial_test import Historial_test
from utils.db import db
from datetime import datetime

from schemas.test import test_schema, tests_schema
from schemas.seccion import seccion_schema, secciones_schema
from schemas.seccion_respuesta import seccion_respuesta_schema, seccion_respuestas_schema
from schemas.historial_test import historial_test_schema,historiales_tests_schema

gestion_test = Blueprint('gestion_test', __name__)

from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.seccion_respuesta import Seccion_respuesta
from model.usuario import Usuario
from model.rango_seccion import Rango_seccion
from model.rango_test import Rango_test
from model.historial_test import Historial_test
from utils.db import db
from datetime import datetime

from schemas.test import test_schema, tests_schema
from schemas.seccion import seccion_schema, secciones_schema
from schemas.seccion_respuesta import seccion_respuesta_schema, seccion_respuestas_schema

gestion_test = Blueprint('gestion_test', __name__)

@gestion_test.route('/gestion_test/v1/realizar_test/<int:id_usuario>', methods=['POST'])
def realizar_test(id_usuario):
    try:
        data = request.json

        # Extraer id_test y id_usuario del JSON
        id_test = data.get('id_test')
        secciones = data.get('secciones', [])

        # Verificar si faltan datos obligatorios en la solicitud
        if not id_test or not id_usuario or not secciones:
            return jsonify({'message': 'Faltan datos obligatorios en la solicitud', 'status': 400}), 400

        # Verificar si el usuario existe
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return jsonify({'message': f'El usuario con ID {id_usuario} no existe', 'status': 404}), 404

        # Verificar si el test existe
        test = Test.query.get(id_test)
        if not test:
            return jsonify({'message': f'El test con ID {id_test} no existe', 'status': 404}), 404

        # Iniciar la transacción
        with db.session.begin():
            puntajes = []
            diagnosticos = []

            for seccion_data in secciones:
                descripcion = seccion_data.get('descripcion')
                respuestas = seccion_data.get('respuestas', [])

                # Calcular puntaje sumando las respuestas de la sección
                puntaje_seccion = sum(respuestas)
                puntajes.append(puntaje_seccion)

                # Buscar diagnóstico basado en los rangos de las tablas rango_seccion y rango_test
                rango_secciones = Rango_seccion.query.filter_by(id_seccion=seccion.id_seccion).all()
                for rango_seccion in rango_secciones:
                    if rango_seccion.minimo <= puntaje_seccion <= rango_seccion.maximo:
                        diagnosticos.append(rango_seccion.diagnostico)

                rango_tests = Rango_test.query.filter_by(id_test=id_test).all()
                for rango_test in rango_tests:
                    if rango_test.minimo <= puntaje_seccion <= rango_test.maximo:
                        diagnosticos.append(rango_test.diagnostico)

                # Convertir listas de puntajes y diagnósticos a cadenas separadas por comas
                puntajes_str = ','.join(map(str, puntajes))
                diagnosticos_str = ','.join(map(str, diagnosticos))

                # Crear una instancia de Seccion_respuesta y agregarla a la sesión
                seccion = Seccion.query.filter_by(descripcion=descripcion, id_test=id_test).first()
                if not seccion:
                    raise ValueError(f"La sección '{descripcion}' para el test ID {id_test} no se encuentra en la base de datos.")

                respuestas_str = ','.join(map(str, respuestas))
                seccion_respuesta = Seccion_respuesta(
                    id_usuario=id_usuario,
                    id_test=id_test,
                    id_seccion=seccion.id_seccion,
                    respuestas=respuestas_str
                )
                db.session.add(seccion_respuesta)

            # Crear un registro en la tabla historial_test
            fecha_realizado = datetime.now()
            nuevo_historial = Historial_test(
                id_usuario=id_usuario,
                id_test=id_test,
                fecha_realizado=fecha_realizado,
                puntaje_realizado=puntajes_str,
                diagnostico=diagnosticos_str
            )
            db.session.add(nuevo_historial)

        # Confirmar todos los cambios en la base de datos
        db.session.commit()

        # Preparar la respuesta JSON con el puntaje realizado y el diagnóstico
        response = {
            'message': 'Test Realizado',
            'status': 201,
            'puntaje_realizado': puntajes_str,
            'diagnostico': diagnosticos_str
        }

        return jsonify(response), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error al registrar respuestas: {str(e)}', 'status': 500}), 500

    



@gestion_test.route('/gestion_test/v1/visualizar_historial_test/<int:id_usuario>', methods=['GET'])
def visualizar_historial_test(id_usuario):
    try:
        historiales = Historial_test.query.filter_by(id_usuario=id_usuario).all()

        if not historiales:
            return jsonify({'message': f'No se encontraron historiales para el usuario con ID {id_usuario}', 'status': 404}), 404

    
        result = historiales_tests_schema.dump(historiales)

        response = {
            'message': 'Historiales de test recuperados correctamente',
            'status': 200,
            'data': result
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'message': f'Error al recuperar historiales de test: {str(e)}', 'status': 500}), 

