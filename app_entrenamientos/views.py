from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Entrenamiento
from .forms import EntrenamientoForm

# Vista para listar todos los entrenamientos
class ListaEntrenamientos(ListView):
    model = Entrenamiento
    template_name = 'app_entrenamientos/entrenamiento_lista.html'
    context_object_name = 'entrenamientos'
    ordering = ['fecha_inicio', 'tipo_entrenamiento']

# Vista para ver los detalles de un entrenamiento específico
class DetalleEntrenamiento(DetailView):
    model = Entrenamiento
    template_name = 'app_entrenamientos/entrenamiento_detalle.html'
    context_object_name = 'entrenamiento'

# Vista para crear un nuevo entrenamiento
class CrearEntrenamiento(CreateView):
    model = Entrenamiento
    form_class = EntrenamientoForm
    template_name = 'app_entrenamientos/entrenamiento_formulario.html'
    success_url = reverse_lazy('app_entrenamientos:lista_entrenamientos')

# Vista para editar un entrenamiento existente
class EditarEntrenamiento(UpdateView):
    model = Entrenamiento
    form_class = EntrenamientoForm
    template_name = 'app_entrenamientos/entrenamiento_formulario.html'
    success_url = reverse_lazy('app_entrenamientos:lista_entrenamientos')

# Vista para borrar un entrenamiento
class BorrarEntrenamiento(DeleteView):
    model = Entrenamiento
    template_name = 'app_entrenamientos/entrenamiento_confirmar_borrar.html'
    context_object_name = 'entrenamiento'
    success_url = reverse_lazy('app_entrenamientos:lista_entrenamientos')