from rest_framework import serializers

from .models import Despacho, Abogado

# ABOGADO
class AbogadoSerial(serializers.ModelSerializer):
    class Meta:
        model = Abogado
        fields = (
            'id',
            'nombre',
            'despacho',
            'locales',
            'federales',
        )

# DESPACHO
class DespachoSerial(serializers.ModelSerializer):
    abogados = AbogadoSerial(many=True, read_only=True)
    class Meta:
        model = Despacho
        fields = (
            'id',
            'nombre',
            'abogados',
        )