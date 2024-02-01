from django.contrib import admin
from .models import Tarea


# Importando las tareas
admin.site.register(Tarea)