from database import db

def guardar_libro(libro):

    db.session.add(libro)
    db.session.commit()