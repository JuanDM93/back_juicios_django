from rest_framework import viewsets

from .models import Acuerdo, Juicio, Juzgado
from .serializers import AcuerdoSerial, JuicioSerial, JuzgadoSerial

# ACUERDO
class AcuerdoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerial

# JUICIO
class JuicioViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Juicio.objects.all()
    serializer_class = JuicioSerial

# JUZGADO
class JuzgadoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Juzgado.objects.all()
    serializer_class = JuzgadoSerial
