from rest_framework import serializers
from contas.models.conta import Conta


class SaldoSerializer(serializers.ModelSerializer):
    """Serializer para saldo"""

    class Meta:
        model = Conta
        fields = ["saldo"]
