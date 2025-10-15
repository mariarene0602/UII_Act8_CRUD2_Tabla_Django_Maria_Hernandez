from django.urls import path
from .views import (
    ListaEntrenamientos,
    DetalleEntrenamiento,
    CrearEntrenamiento,
    EditarEntrenamiento,
    BorrarEntrenamiento
)

app_name = 'app_entrenamientos'

urlpatterns = [
    path('', ListaEntrenamientos.as_view(), name='lista_entrenamientos'),
    path('crear/', CrearEntrenamiento.as_view(), name='crear_entrenamiento'),
    path('<int:pk>/', DetalleEntrenamiento.as_view(), name='detalle_entrenamiento'),
    path('<int:pk>/editar/', EditarEntrenamiento.as_view(), name='editar_entrenamiento'),
    path('<int:pk>/borrar/', BorrarEntrenamiento.as_view(), name='borrar_entrenamiento'),
]