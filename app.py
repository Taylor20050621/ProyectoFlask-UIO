import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from database import init_db

#IMPORTAR LOS BLUEPRINTS
from routes.libro_routes import libros_bp

# 1. CARGAR VARIABLES DE ENTRONO DESDE .env (PRIMERA LINEA DE PROTECCION)

load_dotenv()

app = Flask(__name__)

# 2. CONSTRUCCION DIDADCTICA DE LA CONEXION CON POSTGRES

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# CONSTRUIR UIR DE LA DATA BASE
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# LA RECETA DE LA URI PARA CONECTARSE
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# =========================================================
# DEBUG (Puedes quitar luego)
# =========================================================
print("===================================")
print("Conectando a PostgreSQL...")
print(f"Base de datos: {DB_NAME}")
print(f"Host: {DB_HOST}")
print("===================================")

# 4. INICIALIZAR LA BASE DE DATOS
init_db(app)


# 5. REGISTRAR LOS BLUEPRINTS

app.register_blueprint(libros_bp)

# 6. Rutasprincipales

@app.route('/')
def home():

    return jsonify({
        "mensaje": "Sistema de Biblioteca funcionando correctamente",
        "estado": "activo"
    })

# =========================================================
# RUTA TEST
# =========================================================
@app.route('/health')
def health():

    return jsonify({
        "status": "ok"
    })


if __name__ == '__main__':
    app.run(debug=True)
