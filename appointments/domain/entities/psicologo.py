# appointments/domain/entities/psicologo.py

from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4

@dataclass
class Psicologo:
    id: UUID
    nombre: str
    apellidos: str
    email: str
    telefono: str
    especialidad: str
    numero_colegiado: str
    activo: bool = True

    @classmethod
    def crear(cls, 
              nombre: str,
              apellidos: str,
              email: str,
              telefono: str,
              especialidad: str,
              numero_colegiado: str) -> 'Psicologo':
        """
        Factory method para crear un nuevo psicólogo
        """
        return cls(
            id=uuid4(),
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono,
            especialidad=especialidad,
            numero_colegiado=numero_colegiado
        )

    def actualizar_datos(self,
                        nombre: Optional[str] = None,
                        apellidos: Optional[str] = None,
                        email: Optional[str] = None,
                        telefono: Optional[str] = None,
                        especialidad: Optional[str] = None) -> None:
        """
        Actualiza los datos del psicólogo
        """
        if nombre:
            self.nombre = nombre
        if apellidos:
            self.apellidos = apellidos
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if especialidad:
            self.especialidad = especialidad

    def desactivar(self) -> None:
        """
        Desactiva el psicólogo
        """
        self.activo = False

    def activar(self) -> None:
        """
        Activa el psicólogo
        """
        self.activo = True