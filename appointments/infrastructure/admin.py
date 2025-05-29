# appointments/infrastructure/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Psicologo, Especialidad

@admin.register(Psicologo)
class PsicologoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'especialidad', 'numero_colegiado', 'activo')
    list_filter = ('activo', 'especialidad')
    search_fields = ('nombre', 'apellidos', 'email', 'numero_colegiado')
    ordering = ('apellidos', 'nombre')
    
    fieldsets = (
        (_('Información Personal'), {
            'fields': ('nombre', 'apellidos', 'email', 'telefono')
        }),
        (_('Información Profesional'), {
            'fields': ('especialidad', 'numero_colegiado')
        }),
        (_('Estado'), {
            'fields': ('activo',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si estamos editando un objeto existente
            return ('id', 'created_at', 'updated_at')
        return ('created_at', 'updated_at')

    def clean(self):
        super().clean()
        # Validaciones personalizadas
        if self.email and Psicologo.objects.filter(email=self.email).exclude(id=self.id).exists():
            raise ValidationError({'email': _('Este email ya está registrado')})
        if self.numero_colegiado and Psicologo.objects.filter(numero_colegiado=self.numero_colegiado).exclude(id=self.id).exists():
            raise ValidationError({'numero_colegiado': _('Este número de colegiado ya está registrado')})

    actions = ['activar_psicologos', 'desactivar_psicologos']

    def activar_psicologos(self, request, queryset):
        queryset.update(activo=True)
    activar_psicologos.short_description = _('Activar psicólogos seleccionados')

    def desactivar_psicologos(self, request, queryset):
        queryset.update(activo=False)
    desactivar_psicologos.short_description = _('Desactivar psicólogos seleccionados')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)