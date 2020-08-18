from django.contrib import admin

from .models import (
    Acuerdo,
    JuicioLocal, JuicioFederal,
    JuzgadoLocal, JuzgadoFederal,
)

# Register your models here.
admin.site.register(Acuerdo)

admin.site.register(JuicioLocal)
admin.site.register(JuicioFederal)

admin.site.register(JuzgadoLocal)
admin.site.register(JuzgadoFederal)