from rest_framework import viewsets

from .models import Abogado, Despacho
from .serializers import AbogadoSerial, DespachoSerial

# DESPACHO
class DespachoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerial

# ABOGADO
class AbogadoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerial