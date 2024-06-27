import json
from flask import Blueprint, request, jsonify
from model.test import Test
from model.seccion import Seccion
from model.seccion_respuesta import Seccion_respuesta
from model.usuario import Usuario
from model.rango_seccion import Rango_seccion
from model.rango_test import Rango_test
from model.historial_test import Historial_test
from schemas.historial_test import historiales_tests_schema
from utils.db import db
from datetime import datetime

gestion_test = Blueprint('gestion_test', __name__)

# Función para crear una respuesta de sección
def crear_seccion_respuesta(id_usuario, id_test, seccion_data):

    id_seccion = seccion_data.get('id_seccion')
    respuestas = seccion_data.get('respuestas', [])

    # Calcular el puntaje sumando las respuestas de la sección
    puntaje_seccion = sum(respuestas)

    # Verificar si la sección existe
    seccion = Seccion.query.get(id_seccion)
    if not seccion:
        raise ValueError(f'La sección con ID {id_seccion} no existe')

    # Buscar diagnóstico basado en los rangos de la tabla rango_seccion
    diagnostico_seccion = next(
        (rango.diagnostico for rango in Rango_seccion.query.filter_by(id_seccion=id_seccion).all()
         if rango.minimo <= puntaje_seccion <= rango.maximo), None)
    
    # Convertir respuestas a cadena
    respuestas_str = ','.join(map(str, respuestas))

    # Crear la instancia de Seccion_respuesta
    seccion_respuesta = Seccion_respuesta(
        id_usuario=id_usuario,
        id_test=id_test,
        id_seccion=id_seccion,
        respuestas=respuestas_str
    )

    return seccion_respuesta, puntaje_seccion, diagnostico_seccion

@gestion_test.route('/gestion_test/v1/realizar_test/<int:id>', methods=['POST'])
def realizar_test(id):
    try:
        data = request.json
        print('data entrante: ', data)

        # Extraer id_test y secciones del JSON
        id_test = data.get('id_test')
        secciones = data.get('secciones', [])

        # Verificar si el usuario existe
        usuario = Usuario.query.get(id)
        if not usuario:
            return jsonify({'message': f'El usuario con ID {id} no existe', 'status': 404}), 404
        
        # Verificar si el test existe
        test = Test.query.get(id_test)
        if not test:
            return jsonify({'message': f'El test con ID {id_test} no existe', 'status': 404}), 404

        puntajes = []
        diagnosticos_seccion = []

        # Iniciar la transacción
        for seccion_data in secciones:
            try:
                seccion_respuesta, puntaje_seccion, diagnostico_seccion = crear_seccion_respuesta(
                    usuario.id_usuario, test.id_test, seccion_data
                )
                
                # Añadir el puntaje a la lista
                puntajes.append(puntaje_seccion)

                # Añadir diagnóstico de sección si existe
                if diagnostico_seccion:
                    diagnosticos_seccion.append(diagnostico_seccion)

                # Agregar la respuesta de sección a la sesión
                db.session.add(seccion_respuesta)

            except ValueError as ve:
                return jsonify({'message': str(ve), 'status': 404}), 404

        # Calcular el puntaje total sumando los puntajes de todas las secciones
        puntaje_total = sum(puntajes)

        # Buscar diagnóstico basado en el rango de la tabla rango_test para el puntaje total
        diagnostico_test = next(
            (rango.diagnostico for rango in Rango_test.query.filter_by(id_test=id_test).all()
                if rango.minimo <= puntaje_total <= rango.maximo), None)

        # Convertir listas de puntajes y diagnósticos a cadenas separadas por comas
        puntajes_str = ','.join(map(str, puntajes))
        diagnosticos_str = ','.join(diagnosticos_seccion)

        # Añadir el puntaje total y el diagnóstico del test a las cadenas existentes
        puntajes_str = f"{puntajes_str},{puntaje_total}" if puntajes_str else str(puntaje_total)
        diagnosticos_str = f"{diagnosticos_str},{diagnostico_test}" if diagnosticos_str else diagnostico_test

        # Crear un registro en la tabla historial_test
        fecha_realizada = datetime.now()
        nuevo_historial = Historial_test(
            id_usuario=usuario.id_usuario,
            id_test=test.id_test,
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

