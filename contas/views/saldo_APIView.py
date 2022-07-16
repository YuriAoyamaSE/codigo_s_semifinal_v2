from rest_framework import generics
from rest_framework.response import Response
from contas.models.conta import Conta
from contas.serializers.saldo_serializer import SaldoSerializer

class SaldoAPIView(generics.ListAPIView):
    """Saldo de uma conta"""

    # def get_queryset(self):
    #     queryset = Conta.objects.filter(id=self.kwargs['pk'])
    #     return queryset

    def get(self, request, *args, **kwargs):
        queryset = Conta.objects.get(id=self.kwargs['pk'])
        return Response(queryset.saldo)
    
    serializer_class = SaldoSerializer
    


# class SaldoViewset(generics.ListAPIView):
#     """Saldo de uma conta"""

#     # def get_queryset(self):
#     #     queryset = Conta.objects.filter(id=self.kwargs['pk'])
#     #     return queryset

#     def get(self, request, *args, **kwargs):
#         queryset = Conta.objects.get(id=self.kwargs['pk'])
#         return Response(queryset.saldo)
    
#     serializer_class = SaldoSerializer
    