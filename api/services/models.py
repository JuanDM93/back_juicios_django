from django.db import models

from api.accounts.models import Abogado

# JUZGADOS
class Juzgado(models.Model):
    # Propiedades
    nombre = models.CharField(max_length=32)

# JUICIOS
class Juicio(models.Model):
    # Propiedades
    nombre = models.CharField(max_length=32)
    fecha = models.DateField()

    # Relaciones
    asignados = models.TextField()

    juzgado = models.ForeignKey(
        Juzgado,
        related_name='juicios',
        on_delete=models.CASCADE
    )    

    class Meta():
        # Latest by ascending order_date. (-descending)
        ordering = ['-juzgado']
        get_latest_by = ['fecha']


# ACUERDOS
class Acuerdo(models.Model):
    # Propiedades  
    nombre = models.CharField(max_length=32)
    contenido = models.TextField()

    # Relaciones
    juicio = models.ForeignKey(
        Juicio,
        related_name='acuerdos',
        on_delete=models.CASCADE
    )
