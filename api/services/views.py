from rest_framework import viewsets

from .models import (
    Acuerdo,
    Juicio, JuicioLocal, JuicioFederal,
    Juzgado
)
from .serializers import (
    AcuerdoSerial,
    JuicioSerial, JuicioLocalSerial, JuicioFederalSerial,
    JuzgadoSerial
)

# ACUERDO
class AcuerdoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerial

# JUICIOs
class JuicioViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Juicio.objects.all()
    serializer_class = JuicioSerial

class JuicioLocalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = JuicioLocal.objects.all()
    serializer_class = JuicioLocalSerial

class JuicioFederalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = JuicioFederal.objects.all()
    serializer_class = JuicioFederalSerial

# JUZGADO
class JuzgadoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Juzgado.objects.all()
    serializer_class = JuzgadoSerial
