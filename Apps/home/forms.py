from django import forms
from .models import Estudiante
from .models import EstudianteAutoriza
from .models import Noticias
from .models import Comentario
from .models import Publicacion
class AlumnoPublicaForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__' 

class AlumnoAutorizaForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutoriza
        fields = '__all__' 

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__' 

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__' 

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__' 

