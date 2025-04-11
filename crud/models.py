from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_created = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


from django.db import models
from django.contrib.auth.models import User

class Venta(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Nuevo campo
    correo = models.EmailField(max_length=100, null=True, blank=True)  # Nuevo campo
    contraseña = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=100, null=True, blank=True)  # Nuevo campo
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servicio.nombre} - {self.cliente}"

    @property
    def ganancia(self):
        # Retorna la diferencia
        return self.precio_venta - self.precio_compra


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Agregado el campo teléfono
    # Puedes agregar más campos según lo que necesites.

    def __str__(self):
        return self.nombre