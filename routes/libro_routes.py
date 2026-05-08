#libro_routes.py

from flask import Blueprint, jsonify, request
from services import libro_service

#Creacion de un blueprint
libros_bp = Blueprint('libros', __name__)

#CRUD de libros

# Crear un libro
@libros_bp.route('/libros', methods=['POST'])
def crear_libro():

    data = request.get_json()

    resultado = libro_service.crear_libro(data)

    if resultado['exito']:
        return jsonify({
            "mensaje": "Libro creado correctamente",
            "libro": resultado['libro'].to_dict()
        }), 201
    else:
        return jsonify({
            "mensaje": "Error al crear el libro",
            "error": resultado['error']
        }), 500 