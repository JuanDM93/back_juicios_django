from rest_framework import viewsets

from .models import (
    Acuerdo,
    JuicioLocal, JuicioFederal,
    Juzgado
)
from .serializers import (
    AcuerdoSerial,
    JuicioLocalSerial, JuicioFederalSerial,
    JuzgadoSerial
)

# ACUERDO
class AcuerdoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerial

# JUICIOs
class JuicioLocalViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = JuicioLocal.objects.all()
    serializer_class = JuicioLocalSerial

class JuicioFederalViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = JuicioFederal.objects.all()
    serializer_class = JuicioFederalSerial


# JUZGADO
class JuzgadoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Juzgado.objects.all()
    serializer_class = JuzgadoSerial
