from rest_framework import viewsets
from contas.models.transacao import Transacao
from contas.serializers.transacao_serializer import TransacaoSerializer

class TransacaoViewset(viewsets.ModelViewSet):
    serializer_class = TransacaoSerializer
    queryset = Transacao.objects.all()
