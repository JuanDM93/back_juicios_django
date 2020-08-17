from django.contrib import admin

from .models import (
    Acuerdo,
    JuicioLocal, JuicioFederal,
    Juzgado
)

# Register your models here.
admin.site.register(Acuerdo)
admin.site.register(JuicioLocal)
admin.site.register(JuicioFederal)
admin.site.register(Juzgado)