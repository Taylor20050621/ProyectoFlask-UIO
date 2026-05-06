import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# 1. CARGAR VARIABLES DE ENTRONO DESDE .env (PRIMERA LINEA DE PROTECCION)

load_dotenv()

app = Flask(__name__)

# 2. CONSTRUCCION DIDADCTICA DE LA CONEXION CON POSTGRES

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# LA RECETA DE LA URI PARA CONECTARSE
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 3. INSTANCIA DE SQLALCHEMY (LA LLAVEMAESTRA)
db = SQLAlchemy(app)

@app.route("/")
def test_connection():
    return jsonify({
        "status": "online",
        "message": "Configuración de base de datos cargada correctamente",
        "user_connected": DB_USER
    })


if __name__ == '__main__':
    app.run(debug=True)
