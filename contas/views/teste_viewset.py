from datetime import date
from rest_framework import generics, request, views, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from contas.models.transacao import Transacao
from contas.serializers.transacao_serializer import TransacaoSerializer

""""testar criar novo caminho e entradas de get: conta, data inicial e data final"""
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
        
        #queryset = queryset.filter(conta_origem=kwargs['conta'])|queryset.filter(conta_destino=kwargs['conta']).order_by('data_transacao')
                
        #queryset = queryset.filter(data_transacao__gte=date.fromisoformat('2022-07-14'), data_transacao__lte=date.fromisoformat('2022-07-15'))

        # if 'data_inicial' in kwargs.keys():
        #     queryset = queryset.filter(data_transacao__gte=date.fromisoformat(kwargs['data_inicial']))
        # if 'data_final' in kwargs.keys():
        #     queryset = queryset.filter(data_transacao__lte=date.fromisoformat(kwargs['data_final']))
            
        # if kwargs['data_inicial'] and kwargs['data_final']:
        #     queryset = queryset.filter(data_transacao__gte=date.fromisoformat(kwargs['data_inicial']), data_transacao__lte=date.fromisoformat(kwargs['data_final']))
        #return queryset

    
