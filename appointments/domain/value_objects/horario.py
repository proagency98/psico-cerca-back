from dataclasses import dataclass

@dataclass
class Horario:
    dia: str
    hora_inicio: str
    hora_fin: str
    activo: bool = True
    