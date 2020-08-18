from rest_framework import viewsets, permissions

from .models import Abogado, Despacho
from .serializers import AbogadoSerial, DespachoSerial

# DESPACHO
class DespachoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerial
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    lookup_field = 'nombre'

# ABOGADO
class AbogadoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerial
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    lookup_field = 'email'