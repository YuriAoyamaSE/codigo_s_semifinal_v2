from rest_framework import generics
from rest_framework.response import Response
from contas.models.conta import Conta
from contas.serializers.saldo_serializer import SaldoSerializer


class SaldoAPIView(generics.ListAPIView):
    """View para devolver saldo de uma conta"""

    def get(self, request, *args, **kwargs):
        queryset = Conta.objects.get(id=self.kwargs["pk"])
        return Response(queryset.saldo)

    serializer_class = SaldoSerializer
