from django.contrib import admin

from .models import (
    Acuerdo,
    Juicio,
    Juzgado,
)

# Register your models here.
admin.site.register(Acuerdo)
admin.site.register(Juicio)
admin.site.register(Juzgado)