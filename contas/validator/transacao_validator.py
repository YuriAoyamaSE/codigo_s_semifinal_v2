import re
from rest_framework import serializers

from contas.models.conta import Conta

def valida_contas(conta_origem, conta_destino):
    """Validacao das contas de origem e de destino"""
    
    try:
        Conta.objects.get(id=conta_origem)
    except:
        raise serializers.ValidationError({'conta_origem': 'Conta origem não existe'})
    try:
        Conta.objects.get(id=conta_destino)
    except:
        raise serializers.ValidationError({'conta_destino': 'Conta destino não existe'})

    if conta_origem == conta_destino:
        raise serializers.ValidationError(
        {'conta_origem, conta_destino': 'Não é possível transação com a mesma conta'})
 
def valida_valor(conta_origem, valor):
    """Validacao do valor da transacao"""

    if valor <= 0:
        raise serializers.ValidationError(
        {'valor': 'Valor da transação não pode ser nulo ou negativo'})

    conta = Conta.objects.get(id=conta_origem)
    if conta.saldo < valor:
        raise serializers.ValidationError(
        {'valor': 'Saldo insuficiente para a transação'})       
    

def valida_data(data):
    """Validacao da data da transacao"""
    padrao_data = re.compile('[0-9]{4}[-][0-9]{2}[-][0-9]')
    if data != None:
        if not re.match(padrao_data, str(data)):
            raise serializers.ValidationError(
        {'data_transacao': 'Data de transação deve ter o formato aaaa-mm-dd'})
