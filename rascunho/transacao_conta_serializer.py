from rest_framework import serializers
from contas.models.conta import Conta
from contas.models.transacao import Transacao


class TransacaoContaSerializer(serializers.ModelSerializer):
    

    def create(self, validated_data):
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