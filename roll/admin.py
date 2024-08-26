from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    pass