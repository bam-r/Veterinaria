from django.contrib import admin
from .models import Mascota, Cita

@admin.register(Mascota)

class MascotaAdmin(admin.ModelAdmin):
    list_display=('nombre','especie','raza','dueño')
    
@admin.register(Cita)

class CitaAdmin(admin.ModelAdmin):
    list_display=('mascota','fecha','hora','motivo','estado')
