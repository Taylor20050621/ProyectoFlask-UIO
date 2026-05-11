from .base import EntidadBase

class Libro(EntidadBase):
    def __init__(self, id: int, titulo: str, autor: str):
        super().__init__(id)
        self._titulo = titulo
        self._autor = autor