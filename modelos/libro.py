from .base import EntidadBase

class Libro(EntidadBase):
    def __init__(self, id: int, titulo: str, autor: str):
        super().__init__(id)
        self._titulo = titulo
        self._autor = autor
    
# Un Método: Una acción que el libro puede realizar
    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} | Autor: {self.autor} | Estado: {estado}"

    def cambiar_disponibilidad(self):
        # Accedemos a 'self.disponible' para modificar SU propio estado
        self.disponible = not self.disponible