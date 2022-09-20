from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import AlumnoPublicaForm
from .forms import AlumnoAutorizaForm
from .forms import ComentarioForm
from .forms import NoticiaForm
from .forms import PublicacionForm

from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
     template_name='Home.html'

class EstudiantesView(TemplateView):
     template_name='estudiantes.html'

class AdministradoresView(TemplateView):
     template_name='administradores.html'   

class NoticiaViews(TemplateView):
     template_name='noticias.html'         

class PublicacionView(TemplateView):
     template_name='publicacion.html'  

class ComentarioView(TemplateView):
     template_name='comentario.html'       

class CrearAlumnoPublicaView(CreateView):
     template_name= 'alumnopublica.html'
     form_class = AlumnoPublicaForm
     success_url = reverse_lazy('home:homeapp')

class CrearAlumnoAutorizaViews(CreateView):
     template_name= 'Alumnoautoriza.html'
     form_class = AlumnoAutorizaForm
     success_url = reverse_lazy('home:homeapp')

class vnoticiasView(CreateView):
     template_name= 'vnoticia.html'
     form_class = NoticiaForm
     success_url = reverse_lazy('home:homeapp')

class vpublicacionView(CreateView):
     template_name= 'vpublicacion.html'
     form_class = PublicacionForm
     success_url = reverse_lazy('home:homeapp')

class vcomentarioView(CreateView):
     template_name= 'vcomentario.html'
     form_class = ComentarioForm
     success_url = reverse_lazy('home:homeapp')     




      