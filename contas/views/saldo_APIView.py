from rest_framework import generics
from rest_framework.response import Response
from contas.models.conta import Conta
from contas.serializers.saldo_serializer import SaldoSerializer


class SaldoAPIView(generics.ListAPIView):
    """View para devolver saldo de uma conta"""

    queryset = Conta.objects.all()
    serializer_class = SaldoSerializer

    def get(self, request, *args, **kwargs):
        queryset = Conta.objects.get(id=self.kwargs["pk"])
        return Response({'saldo':queryset.saldo})
