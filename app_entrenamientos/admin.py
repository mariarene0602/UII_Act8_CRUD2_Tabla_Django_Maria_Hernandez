from django.contrib import admin
from .models import Entrenamiento

@admin.register(Entrenamiento)
class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tipo_entrenamiento',
        'fecha_inicio',
        'fecha_fin',
        'activo',
        'fecha_creacion',
    )
    list_filter = ('activo', 'fecha_inicio', 'fecha_fin')
    search_fields = ('tipo_entrenamiento', 'descripcion')
    date_hierarchy = 'fecha_inicio' 

    fieldsets = (
        (None, {
            'fields': ('tipo_entrenamiento', 'descripcion')
        }),
        ('Fechas del Entrenamiento', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )