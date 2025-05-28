from dataclasses import dataclass

@dataclass
class Especialidad:
    nombre: str
    activo: bool = True
    