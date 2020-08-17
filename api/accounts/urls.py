from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import DespachoViewSet, AbogadoViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'despachos', DespachoViewSet)
router.register(r'abogados', AbogadoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]