from django.db import models

class task(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField(blank=True)
     is_created = models.BooleanField(default=False)
     created = models.DateTimeField(auto_now=True)


class Meta:
     ordering = ['-created']

     def __str__(self):
          return self.title
     
     from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
   

