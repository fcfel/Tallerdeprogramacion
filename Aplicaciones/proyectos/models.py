from django.db import models

# Create your models here.
class Proyecto(models.Model):

    date = models.DateTimeField(auto_now=True)
    codigo = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField( max_length=2000 )
    publish = models.BooleanField(default=True)
    imageproj = models.ImageField(upload_to= 'proyectos_imagenes/', null=True)

    def __str__(self):
        texto = "[{0}] {1}"
        if self.publish:
            tp = "On"
        else:
            tp = "Off"    
        return texto.format(self.nombre,tp)