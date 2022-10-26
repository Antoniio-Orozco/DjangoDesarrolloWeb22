"""ColegioSanJose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from Apps.home import views     
from .views import HomeView,EstudiantesView,AdministradoresView,CrearAlumnoPublicaView,CrearAlumnoAutorizaViews,NoticiaViews,PublicacionView,ComentarioView
from .views import vnoticiasView,vpublicacionView,vcomentarioView,RegistroView,LoginView
from .views import ListarEstudianteView,ListarEstudianteAutorizaView,ListarNoticiaView,ListarPublicacionView,ListarComentarioView,EditarAlumnoPublicaView,EditarAlumnoAutorizaViews
from .views import EditarnoticiasView,EditarpublicacionView,EditarcomentarioView,EstudianteDetailView,EstudianteAutorizaDetailView
from .views import NoticiasDetailView,PublicacionDetailView,ComentarioDetailView
app_name='home'

urlpatterns = [
      path('', HomeView.as_view(), name='homeapp'),
      path('estudiantes/', EstudiantesView.as_view(), name='estudiantesapp'),
      path('administradores/', AdministradoresView.as_view(), name='administradoresapp'),
      path('crearEstudiante/', CrearAlumnoPublicaView.as_view(), name='CrearEstudiante'),
      path('crearEstudiantePublica/', CrearAlumnoAutorizaViews.as_view(), name='CrearEstudiantePublica'),
      path('Noticia/', NoticiaViews.as_view(), name='Noticiaapp'),  
      path('Publicacion/', PublicacionView.as_view(), name='Publicacionapp'),   
      path('Comentario/', ComentarioView.as_view(), name='Comentarioapp'),    
      path('CrearNoticia/', vnoticiasView.as_view(), name='CrearNoticia'),   
      path('CrearPublicacion/', vpublicacionView.as_view(), name='CrearPublicacion'),  
      path('CrearComentario/', vcomentarioView.as_view(), name='CrearComentario'),  
       path('registro/', RegistroView.as_view(), name='Registro'), 
       path('login/', LoginView.as_view(), name='login'),     
        path('listado_estudiante/', ListarEstudianteView.as_view(), name='listadoest'), 
        path('listado_estudianteAutoriza/', ListarEstudianteAutorizaView.as_view(), name='listadoestAuto'),    
        path('listado_noticia/', ListarNoticiaView.as_view(), name='listadonoticia'),    
        path('listado_publicacion/', ListarPublicacionView.as_view(), name='listadopublicacion'),   
        path('listado_comentario/', ListarComentarioView.as_view(), name='listadocomentario'), 
         path('editar_estudiante/<int:pk>', EditarAlumnoPublicaView.as_view(), name='editarest'),  
         path('editar_estudianteAutoriza/<int:pk>', EditarAlumnoAutorizaViews.as_view(), name='editarestAuto'),  
         path('editar_noticia/<int:pk>', EditarnoticiasView.as_view(), name='editarNoticia'),  
         path('editar_publicacion/<int:pk>', EditarpublicacionView.as_view(), name='editarPublicacion'),  
         path('editar_comentario/<int:pk>', EditarcomentarioView.as_view(), name='editarComentario'),  
           path('Estudiante_Detail/<int:pk>', EstudianteDetailView.as_view(), name='estudianteDet'),  
           path('EstudianteAutoriza_Detail/<int:pk>', EstudianteAutorizaDetailView.as_view(), name='estudianteAutoDet'),  
           path('Noticia_Detail/<int:pk>', NoticiasDetailView.as_view(), name='noticiaDet'),
           path('Publicacion_Detail/<int:pk>', PublicacionDetailView.as_view(), name='publicacionDet'),
           path('Comentario_Detail/<int:pk>', ComentarioDetailView.as_view(), name='comentarioDet'),
]          
