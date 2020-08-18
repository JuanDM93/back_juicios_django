from rest_framework import viewsets

from .models import (
    Acuerdo,
    Juicio,
    Juzgado,
)
from .serializers import (
    AcuerdoSerial,
    JuicioSerial,
    JuzgadoSerial,
)

# ACUERDO
class AcuerdoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerial

# JUICIO
class JuicioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Juicio.objects.all()
    serializer_class = JuicioSerial

# JUZGADO
class JuzgadoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `retrieve` actions.
    """
    queryset = Juzgado.objects.all()
    serializer_class = JuzgadoSerial
