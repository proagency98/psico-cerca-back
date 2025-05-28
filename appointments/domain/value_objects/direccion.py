from dataclasses import dataclass

@dataclass
class Direccion:
    calle: str
    numero: str
    ciudad: str
    pais: str
    codigo_postal: str
    activo: bool = True
    