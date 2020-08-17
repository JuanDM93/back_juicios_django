from rest_framework import serializers

from api.accounts.serializers import AbogadoSerial
from .models import (
    Juzgado,
    Juicio, JuicioLocal, JuicioFederal,
    Acuerdo
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
        )

class JuicioFederalSerial(JuicioSerial):
    abogados = AbogadoSerial(many=True, read_only=True)
    acuerdos = AcuerdoSerial(many=True, read_only=True)
    class Meta:
        model = JuicioFederal
        fields = (
            'id',
            'nombre',
            'tipo',
            'juzgado',
            'abogados',
            'acuerdos',
            'extraFederal',
        )

class JuicioLocalSerial(JuicioSerial):
    abogados = AbogadoSerial(many=True, read_only=True)
    acuerdos = AcuerdoSerial(many=True, read_only=True)
    class Meta:
        model = JuicioLocal
        fields = (
            'id',
            'nombre',
            'tipo',
            'abogados',
            'acuerdos',
            'juzgado',
            'extraLocal',
        )

# JUZGADO
class JuzgadoSerial(serializers.ModelSerializer):
    juicios = JuicioSerial(many=True, read_only=True)
    class Meta:
        model = Juzgado
        fields = (
            'id',
            'nombre',
            'juicios',
        )