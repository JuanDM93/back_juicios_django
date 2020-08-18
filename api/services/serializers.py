from rest_framework import serializers

from api.accounts.serializers import AbogadoSerial
from .models import (
    Juzgado, JuzgadoLocal, JuzgadoFederal,
    Juicio, JuicioLocal, JuicioFederal,
    Acuerdo,
)

# ACUERDO
class AcuerdoSerial(serializers.ModelSerializer):
    class Meta:
        model = Acuerdo
        fields = (
            'id',
            'nombre',
            'juicio',
            'contenido',
        )

# JUICIOs
class JuicioLocalSerial(serializers.ModelSerializer):
    abogados = AbogadoSerial(many=True, read_only=True)
    acuerdos = AcuerdoSerial(many=True, read_only=True)
    class Meta:
        model = JuicioLocal
        fields = (
            'id',
            'nombre',
            'juzgado',
            'abogados',
            'acuerdos',
            'extraLocal',
        )

class JuicioFederalSerial(serializers.ModelSerializer):
    abogados = AbogadoSerial(many=True, read_only=True)
    acuerdos = AcuerdoSerial(many=True, read_only=True)
    class Meta:
        model = JuicioFederal
        fields = (
            'id',
            'nombre',
            'juzgado',
            'abogados',
            'acuerdos',
            'extraFederal',
        )

# JUZGADOs
class JuzgadoLocalSerial(serializers.ModelSerializer):
    juicios = JuicioLocalSerial(many=True, read_only=True)
    class Meta:
        model = JuzgadoLocal
        fields = (
            'id',
            'nombre',
            'juicios',
            'extraLocal',
        )
        
class JuzgadoFederalSerial(serializers.ModelSerializer):
    juicios = JuicioFederalSerial(many=True, read_only=True)
    class Meta:
        model = JuzgadoFederal
        fields = (
            'id',
            'nombre',
            'juicios',
            'extraFederal',
        )