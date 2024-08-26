"""
URL configuration for happytails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roll.views import signup, signout, signin
from main.views import index, base, contacto, nosotros, servicios, editar_cliente, citas
from agenda.views import CitaCreateView, CitaListView, CitaDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('base/', base, name="base"),
    path('servicios/', servicios, name="servicios"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('logout/', signout, name="logout"),
    path('signin/', signin, name="signin"),
    path('agendar_hora/', CitaCreateView.as_view(), name="agendar"),
    path('lista_citas/', CitaListView.as_view(), name="lista_citas"),
    path('eliminar_cita/<int:pk>/', CitaDeleteView.as_view(), name='eliminar_cita'),


    path('editar_cliente/', editar_cliente, name='editar_cliente'),
    path('citas/', citas, name='citas'),

    path('pacientes/', include('pacientes.urls')),
]
