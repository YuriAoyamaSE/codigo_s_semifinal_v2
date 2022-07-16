from django.db import models
from django.utils import timezone


class Transacao(models.Model):
    """model para transacao entre contas"""

    conta_origem = models.IntegerField()
    conta_destino = models.IntegerField()
    valor = models.FloatField()
    data_transacao = models.DateField(default=timezone.localdate)
