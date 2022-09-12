from django.db import models

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



