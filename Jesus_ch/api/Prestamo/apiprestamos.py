# API


from flask import Blueprint, jsonify
from Config.db import app, db, ma
from Models.Prestamo import Prestamo, PrestamoSchema

ruta_prestamo = Blueprint("routes_prestamo", __name__)

prestamo_schema   = PrestamoSchema()
prestamos_schemas = PrestamoSchema(many=True)

@ruta_prestamo.route('/prestamo', methods=['GET'])
def clientes():
    resultall = Prestamo.query.all()
    resultPrestamo = prestamos_schemas.dump(resultall)
    return jsonify(resultPrestamo)
