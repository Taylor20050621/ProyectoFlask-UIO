from . import db

class Tarea(db.Model):
    # 1. Definimos la tabla en PostgreSQL
    __tablename__ = 'tareas' 

    # 2. Definimos las Columnas
    # El ID es la llave primaria y debe autogenerarse
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True) # Usamos Text para descripciones largas
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(20), default='Pendiente') # Pendiente, En Proceso, Completada
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)    


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Relación: Un usuario tiene muchas tareas
    tareas = db.relationship('Tarea', backref='autor', lazy=True)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "email": self.email}

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre}