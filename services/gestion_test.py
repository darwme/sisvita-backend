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
from schemas.historial_test import historial_test_schema, historiales_tests_schema

gestion_test = Blueprint('gestion_test', __name__)


@gestion_test.route('/gestion_test/v1/realizar_test/<int:id_usuario>', methods=['POST'])
def realizar_test(id_usuario):
    try:
        data = request.json

        # Extraer id_test y secciones del JSON
        id_test = data.get('id_test')
        secciones = data.get('secciones', [])

        # Verificar si el usuario existe
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return jsonify({'message': f'El usuario con ID {id_usuario} no existe', 'status': 404}), 404

        # Verificar si el test existe
        test = Test.query.get(id_test)
        if not test:
            return jsonify({'message': f'El test con ID {id_test} no existe', 'status': 404}), 404

        puntajes = []
        diagnosticos = []

        # Iniciar la transacción fuera del bucle de secciones
        with db.session.begin():
            for seccion_data in secciones:
                id_seccion = seccion_data.get('id_seccion')
                respuestas = seccion_data.get('respuestas', [])

                # Calcular puntaje sumando las respuestas de la sección
                puntaje_seccion = sum(respuestas)
                puntajes.append(puntaje_seccion)

                # Verificar si la sección existe
                seccion = Seccion.query.get(id_seccion)
                if not seccion:
                    return jsonify({'message': f'La sección con ID {id_seccion} no existe', 'status': 404}), 404

                # Buscar diagnóstico basado en los rangos de las tablas rango_seccion y rango_test
                diagnostico_seccion = next(
                    (rango.diagnostico for rango in Rango_seccion.query.filter_by(id_seccion=id_seccion).all()
                     if rango.minimo <= puntaje_seccion <= rango.maximo), None)
                
                if diagnostico_seccion:
                    diagnosticos.append(diagnostico_seccion)

                diagnostico_test = next(
                    (rango.diagnostico for rango in Rango_test.query.filter_by(id_test=id_test).all()
                     if rango.minimo <= puntaje_seccion <= rango.maximo), None)

                if diagnostico_test:
                    diagnosticos.append(diagnostico_test)

                respuestas_str = ','.join(map(str, respuestas))
                seccion_respuesta = Seccion_respuesta(
                    id_usuario=id_usuario,
                    id_test=id_test,
                    id_seccion=id_seccion,
                    respuestas=respuestas_str
                )
                db.session.add(seccion_respuesta)

            # Convertir listas de puntajes y diagnósticos a cadenas separadas por comas
            puntajes_str = ','.join(map(str, puntajes))
            diagnosticos_str = ','.join(diagnosticos)

            # Crear un registro en la tabla historial_test
            fecha_realizada = datetime.now()
            nuevo_historial = Historial_test(
                id_usuario=id_usuario,
                id_test=id_test,
                fecha_realizada=fecha_realizada,
                puntajes=puntajes_str,
                diagnosticos=diagnosticos_str
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

