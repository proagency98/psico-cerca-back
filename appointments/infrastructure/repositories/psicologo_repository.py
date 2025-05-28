# appointments/infrastructure/repositories/psicologo_repository.py
from typing import List, Optional
from uuid import UUID

from appointments.domain.entities.psicologo import Psicologo
from appointments.infrastructure.models import Psicologo as PsicologoModel

class PsicologoRepository:
    @staticmethod
    def to_entity(model: PsicologoModel) -> Psicologo:
        return Psicologo(
            id=model.id,
            nombre=model.nombre,
            apellidos=model.apellidos,
            email=model.email,
            telefono=model.telefono,
            especialidad=model.especialidad,
            numero_colegiado=model.numero_colegiado,
            activo=model.activo
        )

    @staticmethod
    def to_model(entity: Psicologo) -> PsicologoModel:
        return PsicologoModel(
            id=entity.id,
            nombre=entity.nombre,
            apellidos=entity.apellidos,
            email=entity.email,
            telefono=entity.telefono,
            especialidad=entity.especialidad,
            numero_colegiado=entity.numero_colegiado,
            activo=entity.activo
        )