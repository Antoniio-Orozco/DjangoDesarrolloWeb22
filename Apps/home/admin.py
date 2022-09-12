from django.contrib import admin
from .models import Estudiante,EstudianteAutoriza,Noticias,Publicacion,Comentario

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(EstudianteAutoriza)
admin.site.register(Noticias)
admin.site.register(Publicacion)
admin.site.register(Comentario)
