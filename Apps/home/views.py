from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import AlumnoPublicaForm, RegistroForm
from .forms import AlumnoAutorizaForm
from .forms import ComentarioForm
from .forms import NoticiaForm
from .forms import PublicacionForm
from .models import Usuario, Estudiante, EstudianteAutoriza, Noticias,Publicacion
from django.contrib.auth.views import LoginView

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
     success_url = reverse_lazy('home:listadoest')

class CrearAlumnoAutorizaViews(CreateView):
     template_name= 'Alumnoautoriza.html'
     form_class = AlumnoAutorizaForm
     success_url = reverse_lazy('home:listadoestAuto')

class vnoticiasView(CreateView):
     template_name= 'vnoticia.html'
     form_class = NoticiaForm
     success_url = reverse_lazy('home:listadonoticia')

class vpublicacionView(CreateView):
     template_name= 'vpublicacion.html'
     form_class = PublicacionForm
     success_url = reverse_lazy('home:listadopublicacion')

class vcomentarioView(CreateView):
     template_name= 'vcomentario.html'
     form_class = ComentarioForm
     success_url = reverse_lazy('home:homeapp')     

class RegistroView(CreateView):
     model = Usuario
     form_class = RegistroForm
     success_url = reverse_lazy('home:homeapp')    

class LoginView(LoginView):
     template_name = 'login.html'
    

class ListarEstudianteView(ListView):
     template_name = 'listarestudiante.html'
     model = Estudiante

def get_querty(self):
     return Estudiante.objects.all()

class ListarEstudianteAutorizaView(ListView):
     template_name = 'listarestudianteautoriza.html'
     model = EstudianteAutoriza

def get_querty(self):
     return EstudianteAutoriza.objects.all()


class ListarNoticiaView(ListView):
     template_name = 'listarnoticia.html'
     model = Noticias

def get_querty(self):
     return Noticias.objects.all()


class ListarPublicacionView(ListView):
     template_name = 'listarpublicacion.html'
     model = Publicacion

def get_querty(self):
     return Publicacion.objects.all()



      