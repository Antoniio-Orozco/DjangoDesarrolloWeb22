from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .forms import AlumnoPublicaForm, RegistroForm
from .forms import AlumnoAutorizaForm
from .forms import ComentarioForm
from .forms import NoticiaForm
from .forms import PublicacionForm
from .models import Usuario, Estudiante, EstudianteAutoriza, Noticias,Publicacion,Comentario
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView

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
     success_url = reverse_lazy('home:listadocomentario')     

class RegistroView(CreateView):
     model = Usuario
     form_class = RegistroForm
     success_url = reverse_lazy('home:homeapp')    

class LoginView(LoginView):
     template_name = 'login.html'
    

class ListarEstudianteView(ListView):
     template_name = 'listarestudiante.html'
     model = Estudiante

     def get_queryset(self):
         bNombre = self.request.GET.get('nombre')
         if(bNombre):
             return Estudiante.objects.filter(nombre__icontains=bNombre)
         else:
             return Estudiante.objects.all()

class ListarEstudianteAutorizaView(ListView):
     template_name = 'listarestudianteautoriza.html'
     model = EstudianteAutoriza

     def get_queryset(self):
         aNombre = self.request.GET.get('nombre')
         if(aNombre):
             return EstudianteAutoriza.objects.filter(nombre__icontains=aNombre)
         else:
             return EstudianteAutoriza.objects.all()

class ListarNoticiaView(ListView):
     template_name = 'listarnoticia.html'
     model = Noticias

     def get_queryset(self):
         nNombre = self.request.GET.get('nombre')
         if(nNombre):
             return Noticias.objects.filter(nombre__icontains=nNombre)
         else:
             return Noticias.objects.all()


class ListarPublicacionView(ListView):
     template_name = 'listarpublicacion.html'
     model = Publicacion

     def get_queryset(self):

          pNoticia = self.request.GET.get('noticia')
          if(pNoticia):
             return Publicacion.objects.filter(noticia__descripcion__icontains=pNoticia)
          else:
             return Publicacion.objects.all()

class ListarComentarioView(ListView):
     template_name = 'listarcomentario.html'
     model = Comentario

     def get_queryset(self):
          bNoticia = self.request.GET.get('noticia')
          if(bNoticia):
             return Comentario.objects.filter(noticia__descripcion__icontains=bNoticia)
          else:
              return Comentario.objects.all()

class EditarAlumnoPublicaView(UpdateView):
     template_name= 'editaralumnopublica.html'
     model = Estudiante
     form_class = AlumnoPublicaForm
     success_url = reverse_lazy('home:listadoest')

class EditarAlumnoAutorizaViews(UpdateView):
     template_name= 'editaralumnoautoriza.html'
     model = EstudianteAutoriza
     form_class = AlumnoAutorizaForm
     success_url = reverse_lazy('home:listadoestAuto')

class EditarnoticiasView(UpdateView):
     template_name= 'editarnoticia.html'
     model = Noticias 
     form_class = NoticiaForm
     success_url = reverse_lazy('home:listadonoticia')

class EditarpublicacionView(UpdateView):
     template_name= 'editarpublicacion.html'
     model = Publicacion
     form_class = PublicacionForm
     success_url = reverse_lazy('home:listadopublicacion')

class EditarcomentarioView(UpdateView):
     template_name= 'editarcomentario.html'
     model = Comentario
     form_class = ComentarioForm
     success_url = reverse_lazy('home:listadocomentario')    

class EstudianteDetailView(DetailView):
     template_name= 'Estudiante_detail.html'
     model = Estudiante
     queryset = Estudiante.objects.all()

class EstudianteAutorizaDetailView(DetailView):
     template_name= 'Estudianteautoriza_detail.html'
     model = EstudianteAutoriza
     queryset = EstudianteAutoriza.objects.all()

class NoticiasDetailView(DetailView):
     template_name= 'noticia_detail.html'
     model = Noticias
     queryset = Noticias.objects.all()

class PublicacionDetailView(DetailView):
     template_name= 'publicacion_detail.html'
     model = Publicacion
     queryset = Publicacion.objects.all()

class ComentarioDetailView(DetailView):
     template_name= 'comentario_detail.html'
     model = Comentario
     queryset = Comentario.objects.all()