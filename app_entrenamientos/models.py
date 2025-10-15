from django.db import models

class Entrenamiento(models.Model):

    tipo_entrenamiento = models.CharField(
        max_length=100,
        help_text="Ej: Obediencia Básica, Agilidad, Guardia y Protección, Socialización, etc."
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text="Descripción detallada del contenido del entrenamiento."
    )
    fecha_inicio = models.DateField(
        help_text="Fecha en que comienza el entrenamiento."
    )
    fecha_fin = models.DateField(
        blank=True,
        null=True,
        help_text="Fecha estimada de finalización del entrenamiento (puede ser nula si es continuo)."
    )

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Entrenamiento de Perro"
        verbose_name_plural = "Entrenamientos de Perros"
        ordering = ['fecha_inicio', 'tipo_entrenamiento'] 

    def __str__(self):
        return f"{self.tipo_entrenamiento} ({self.fecha_inicio} - {self.fecha_fin if self.fecha_fin else 'Indefinido'})"