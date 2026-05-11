#__init__.py
from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la DB
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    # Comentado para que no crree las tablas cada vez que se inicia la app, solo se deben crear una vez

    # Creamos las tablas en la base de datos 
    #with app.app_context():
       # print("Inicializando BD...")  # DEBUG

        #from .models import Usuario, Categoria, Libro, Prestamo, Cliente

        #db.create_all()

        #print("Tablas creadas con éxito") # DEBUG
        