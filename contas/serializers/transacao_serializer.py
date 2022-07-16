from rest_framework import serializers
from contas.models.conta import Conta
from contas.models.transacao import Transacao
from contas.validator.transacao_validator import (
    valida_contas,
    valida_valor,
    valida_data,
)


class TransacaoSerializer(serializers.ModelSerializer):
    """Serializer para transacao"""

    def validate(self, data):
        """Validacao dos atributos de uma transacao"""
        valida_contas(data.get("conta_origem"), data.get("conta_destino"))
        valida_valor(data.get("conta_origem"), data.get("valor"))
        valida_data(data.get("data_transacao"))

        return data

    def create(self, validated_data):
        """POST de nova transacao valida"""
        destino = Conta.objects.get(id=validated_data["conta_destino"])
        destino.saldo += validated_data["valor"]
        destino.save()

        origem = Conta.objects.get(id=validated_data["conta_origem"])
        origem.saldo -= validated_data["valor"]
        origem.save()
        return super().create(validated_data)

    class Meta:
        model = Transacao
        fields = "__all__"
