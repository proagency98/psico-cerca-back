from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .infrastructure.models import Psicologo, Especialidad

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
            'fields': ('especialidad', 'numero_colegiado', 'descripcion', 'precio')
        }),
        (_('Estado'), {
            'fields': ('activo',)
        }),
        (_('Imagen'), {
            'fields': ('foto',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si estamos editando un objeto existente
            return ('id', 'created_at', 'updated_at')
        return ('created_at', 'updated_at') 

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    fieldsets = (
        (_('Información de la Especialidad'), {
            'fields': ('nombre', 'descripcion')
        }),
        (_('Estado'), {
            'fields': ('activo',)
        }),
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id', 'created_at', 'updated_at')
        return ('created_at', 'updated_at')