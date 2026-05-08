from repositories.libro_repository import guardar_libro
from database.models import Categoria, Libro

def crear_libro(data):

    if data['stock', 0] < 0:
        raise ValueError("El stock no puede ser negativo")

    libro = Libro(
        titulo=data['titulo'],
        autor=data['autor'],
        editorial=data['editorial'],
        anio=data['anio'],
        isbn=data['isbn'],
        stock=data['stock'],
        categoria_id=data['categoria_id'],
        usuario_id=data['usuario_id']
    )

    guardar_libro(libro)

    return libro.to_dict()