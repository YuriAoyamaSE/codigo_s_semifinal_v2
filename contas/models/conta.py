from django.db import models


class Conta(models.Model):
    cliente = models.CharField(max_length=200)
    saldo = models.FloatField(default=0)
    