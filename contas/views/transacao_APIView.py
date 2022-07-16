from datetime import date
from rest_framework import generics
from contas.models.transacao import Transacao
from contas.serializers.transacao_serializer import TransacaoSerializer


class TransacaoAPIView(generics.ListAPIView):
    serializer_class = TransacaoSerializer
    
    def get_queryset(self):
        queryset = Transacao.objects.all().order_by('data_transacao')
        conta = self.request.query_params.get('conta')
        data_inicial = self.request.query_params.get('data_inicial')
        data_final = self.request.query_params.get('data_final')
        if conta:
            queryset = queryset.filter(conta_origem=conta) | queryset.filter(conta_destino=conta)
        if data_inicial:
            queryset = queryset.filter(data_transacao__gte=date.fromisoformat(data_inicial))
        if data_final:
            queryset = queryset.filter(data_transacao__lte=date.fromisoformat(data_final))

        return queryset
