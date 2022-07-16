from django.contrib import admin
from contas.models.conta import Conta
from contas.models.transacao import Transacao

admin.site.register(Conta)
admin.site.register(Transacao)
