from rest_framework import viewsets

from .models import (
    Acuerdo,
    JuicioLocal, JuicioFederal,
    JuzgadoLocal, JuzgadoFederal,
)
from .serializers import (
    AcuerdoSerial,
    JuicioLocalSerial, JuicioFederalSerial,
    JuzgadoLocalSerial, JuzgadoFederalSerial,
)

# ACUERDO
class AcuerdoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerial

# JUICIOs
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
class JuzgadoLocalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = JuzgadoLocal.objects.all()
    serializer_class = JuzgadoLocalSerial

class JuzgadoFederalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = JuzgadoFederal.objects.all()
    serializer_class = JuzgadoFederalSerial
