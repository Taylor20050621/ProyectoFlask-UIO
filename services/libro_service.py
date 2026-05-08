#libro_service.py 

from repositories import libro_repository
from database.models import Libro

def crear_libro(data):

    try:

        if data.get('stock', 0) < 0:
            return {
                "exito": False,
                "error": "El stock no puede ser negativo"
            }

        nuevo_libro = Libro(
            titulo=data['titulo'],
            autor=data['autor'],
            editorial=data['editorial'],
            anio=data['anio'],
            isbn=data['isbn'],
            stock=data['stock'],
            categoria_id=data['categoria_id'],
            usuario_id=data['usuario_id']
        )

        libro_repository.guardar_libro(nuevo_libro)

        return {
            "exito": True,
            "libro": nuevo_libro
        }

    except Exception as e:

        return {
            "exito": False,
            "error": str(e)
        }