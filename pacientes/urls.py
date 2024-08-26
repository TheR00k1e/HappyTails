from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.ver_paciente, name='ver_paciente'),
    path('crear/', views.crear_editar_paciente, name='crear_paciente'),
    path('editar/<int:paciente_id>/', views.crear_editar_paciente, name='editar_paciente'),
    path('eliminar/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
]
