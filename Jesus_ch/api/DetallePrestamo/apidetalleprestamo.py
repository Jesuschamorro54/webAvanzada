# API

from flask import Blueprint, jsonify
from Config.db import app, db, ma
from Models.DetallePrestamo import DetallePrestamo, DetallePrestamoSchema

ruta_detalleprestamo = Blueprint("routes_detalleprestamo", __name__)

detalleprestamo_schema   = DetallePrestamoSchema()
detallesprestamos_schemas = DetallePrestamoSchema(many=True)

@ruta_detalleprestamo.route('/prestamista', methods=['GET'])
def clientes():
    resultall = DetallePrestamo.query.all()
    resultDetalleprestamo = detallesprestamos_schemas.dump(resultall)
    return jsonify(resultDetalleprestamo)
