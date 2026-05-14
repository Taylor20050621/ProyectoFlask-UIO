#libro_repository.py
from database import db
from database.models import Libro


def guardar_libro(libro):

    db.session.add(libro)
    db.session.commit()
    return libro
