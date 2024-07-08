from flask import Blueprint, request, jsonify, make_response
from model.historial_test import Historial_test
from utils.db import db
from schemas.historial_test import historial_test_schema, historiales_tests_schema
from schemas.historial_tests import historial_test_e_schema, historiales_tests_e_schema
from datetime import datetime
import secrets
import string


gestor_historial_test = Blueprint('gestor_historial_test', __name__)


#mostrar los historiales test segun id de usuario
@gestor_historial_test.route('/gestor_historial_test/v1/paciente/listar_h_test/<int:id>', methods=['GET'])
def obtener_historiales_test_usuario(id):
    historiales_tests = Historial_test.query.filter_by(id_usuario=id).all()

    if not historiales_tests:
        data = {
            'message': 'Historiales tests no encontrados',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = historiales_tests_schema.dump(historiales_tests)

    return make_response(jsonify(result), 200)


# Listar todos los historiales de test para el especialista ----------------------------------------
@gestor_historial_test.route('/gestor_historial_test/v1/especialista/listar_h_pacientes', methods=['GET'])
def listar_historiales_test_para_espcialista():
    all_historiales = Historial_test.query.all()
    result = historiales_tests_e_schema.dump(all_historiales)
    
    return make_response(jsonify(result), 200)