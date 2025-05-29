from dataclasses import dataclass
from datetime import datetime

class Especialidad:
    def __init__(self, id: int, nombre: str, descripcion: str, activo: bool = True, created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.activo = activo
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return self.nombre
