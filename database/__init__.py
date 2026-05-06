from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


# Creamos la instancia de la DB
db = SQLAlchemy()

def init_db(app):
    # Traemos la URL del .env que ya configuramos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Unir la base de datos con la aplicacion
    db.init_app(app)

    # Creamos las tablas en la base de datos 
    with app.app_context():
        from .models import Tarea
        db.create_all()
        print("¡Base de datos creada!")
        