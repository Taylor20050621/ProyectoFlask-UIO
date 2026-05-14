#libro_repository.py
from database import db
from database.models import Libro

# =========================================================
# El repository SOLO se comunica con la base de datos.
#
# Aquí:
# ✅ usamos SQLAlchemy
# ✅ hacemos consultas SQL
# ✅ guardamos datos
#
# PERO:
# ❌ NO validamos negocio
# ❌ NO usamos Flask
# ❌ NO usamos jsonify
# =========================================================

def guardar_libro(libro):

    db.session.add(libro)
    db.session.commit()
    return libro


# =========================================================
# OBTENER TODOS LOS LIBROS
# =========================================================
def obtener_libros():

    return Libro.query.all() 

# =========================================================
# OBTENER LIBRO POR ID
# =========================================================
def obtener_por_id(id):

    return Libro.query.get(id)

# =========================================================
# ACTUALIZAR LIBRO
# =========================================================
# SQLAlchemy detecta automáticamente los cambios
# realizados sobre el objeto.
#
# Solo necesitamos hacer commit().
# =========================================================
def actualizar_libro():

    db.session.commit()

# =========================================================
# ELIMINAR LIBRO
# =========================================================
def eliminar_libro(libro):

    db.session.delete(libro)

    db.session.commit()