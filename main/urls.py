# main/urls.py
from django.urls import path
from . import views  # Importa directamente las vistas desde el archivo views.py

urlpatterns = [
    path('editar_cliente/', views.editar_cliente, name='editar_cliente'),  # Ruta para editar cliente
    
]
