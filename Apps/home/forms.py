from django import forms
from .models import Estudiante
from .models import EstudianteAutoriza
from .models import Noticias
from .models import Comentario
from .models import Publicacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140,required=True)
    last_name = forms.CharField(max_length =140, required=False)
    email = forms.EmailField(required=True)       
    
    class Meta:
        model = User
        fields = (
                  'username',
                  'email',
                  'first_name',
                  'last_name', 
                  'password1',
                  'password2', 
        )
