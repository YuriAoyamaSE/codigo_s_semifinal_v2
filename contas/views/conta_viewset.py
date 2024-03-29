from rest_framework import viewsets, serializers
from contas.models.conta import Conta
from contas.serializers.conta_serializer import ContaSerializer


class ContaViewset(viewsets.ModelViewSet):
    """Viewset para contas"""

    serializer_class = ContaSerializer
    queryset = Conta.objects.all()
