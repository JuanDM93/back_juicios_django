from django.db import models
from django.contrib.auth.models import User

# DESPACHOS
class Despacho(models.Model):
    nombre = models.CharField(max_length=32)

# USUARIOS
class Usuario(User):
    # Propiedades
    nombre = models.CharField(max_length=32)

class Abogado(Usuario):
    # Relaciones
    despacho = models.ForeignKey(
        Despacho,
        related_name='abogados',
        on_delete=models.CASCADE
    )
    class Meta():
        ordering = ['despacho']

class DespachoAdmin(Abogado):
    # Propiedades
    telefono = models.CharField(max_length=10)