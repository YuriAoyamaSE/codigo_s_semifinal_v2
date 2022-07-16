from rest_framework import serializers
from contas.models.conta import Conta


class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['saldo']
