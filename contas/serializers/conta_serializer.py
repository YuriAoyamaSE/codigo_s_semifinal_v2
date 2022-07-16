from rest_framework import serializers
from contas.models.conta import Conta
from contas.validator.conta_validator import valida_cliente, valida_saldo


class ContaSerializer(serializers.ModelSerializer):
    """Serializer para contas"""

    class Meta:
        model = Conta
        fields = "__all__"

    def validate(self, data):
        """Validar atributos da conta"""

        valida_cliente(data.get("cliente"))
        valida_saldo(data.get("saldo"))

        return data
