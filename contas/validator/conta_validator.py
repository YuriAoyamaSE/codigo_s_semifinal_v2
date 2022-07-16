import re
from rest_framework import serializers

def valida_cliente(cliente):
    """Validacao do nome do cliente"""
    padrao_nome = re.compile('^[\w\s]+$')

    if re.search(r'\d', cliente):
        raise serializers.ValidationError(
        {'cliente': 'Nome do cliente não pode ter números'})
    if not re.match(padrao_nome, cliente):
        raise serializers.ValidationError(
        {'cliente': 'Nome do cliente não pode caracteres especiais'})
    
def valida_saldo(saldo):
    if saldo < 0:
        raise serializers.ValidationError(
        {'saldo': 'Saldo não pode ser negativo'})
