from rest_framework import serializers

from api.accounts.serializers import AbogadoSerial
from .models import (
    Juzgado,
    Juicio,
    Acuerdo,
)

class AcuerdoSerial(serializers.ModelSerializer):
    class Meta:
        model = Acuerdo
        fields = (
            'id',
            'nombre',
            'juicio',
            'contenido',
        )

class JuicioSerial(serializers.ModelSerializer):
    abogados = AbogadoSerial(many=True, read_only=True)
    acuerdos = AcuerdoSerial(many=True, read_only=True)
    class Meta:
        model = Juicio
        fields = (
            'id',
            'nombre',
            'juzgado',
            'abogados',
            'acuerdos',
            'extraLocal',
        )
        
class JuzgadoSerial(serializers.ModelSerializer):
    juicios = JuicioSerial(many=True, read_only=True)
    class Meta:
        model = Juzgado
        fields = (
            'id',
            'nombre',
            'juicios',
            'localExtra',
        )