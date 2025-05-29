from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Psicologo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=255, verbose_name=_("Nombre"))
    apellidos = models.CharField(max_length=255, verbose_name=_("Apellidos"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    telefono = models.CharField(max_length=20, verbose_name=_("Teléfono"))
    especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE, verbose_name=_("Especialidad"))
    numero_colegiado = models.CharField(max_length=20, unique=True, verbose_name=_("Número de Colegiado"))
    activo = models.BooleanField(default=True, verbose_name=_("Activo"))
    foto = models.ImageField(upload_to='psicologos/', null=True, blank=True, verbose_name=_("Foto"))
    descripcion = models.TextField(verbose_name=_("Descripción"))
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Última actualización"))

    class Meta:
        verbose_name = _("Psicólogo")
        verbose_name_plural = _("Psicólogos")
        ordering = ["apellidos", "nombre"]

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"
        
class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=255, verbose_name=_("Nombre"))
    descripcion = models.TextField(verbose_name=_("Descripción"), null=True, blank=True)
    activo = models.BooleanField(default=True, verbose_name=_("Activo"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Última actualización"))
    
    class Meta:
        verbose_name = _("Especialidad")
        verbose_name_plural = _("Especialidades")
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre