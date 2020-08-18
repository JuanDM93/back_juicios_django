from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import (
    AcuerdoViewSet,
    JuicioViewSet,
    JuzgadoViewSet,
)


app_name = 'locals'
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'acuerdos', AcuerdoViewSet)
router.register(r'juicios', JuicioViewSet)
router.register(r'juzgados', JuzgadoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]