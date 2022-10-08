from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Carne = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre,self.apellido,self.Carne)

class EstudianteAutoriza(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Carne = models.CharField(max_length=15)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre,self.apellido,self.Carne)


class Noticias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s ' % (self.nombre,self.descripcion)

class Publicacion(models.Model):
    numero = models.CharField(max_length=100)
    noticia = models.ForeignKey(Noticias,on_delete=models.CASCADE)
    estudiantepublica = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    estudianteautoriza = models.ForeignKey(EstudianteAutoriza,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.numero,self.noticia,self.estudiantepublica,self.estudianteautoriza)

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticias,on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=100)
    estudiantepublica = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s ' % (self.noticia,self.Descripcion,self.estudiantepublica)

class Usuario(models.Model):
    perfil = models.OneToOneField(User,on_delete=models.CASCADE)    

    def __str__(self):
        return self.perfil.username

    @receiver(post_save, sender=User)
    def crear_usuario(sender, instance, created, **kwargs):
            if created:
                Usuario.objects.create(perfil=instance)

    @receiver(post_save, sender=User)
    def guardar_usuario(sender, instance, created, **kwargs):
             instance.usuario.save()
