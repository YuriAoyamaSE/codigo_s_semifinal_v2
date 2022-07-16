from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from contas.models.transacao import Transacao


class TransacaoTestCase(TestCase):

    fixtures = ["db_para_testes"]

    def setUp(self) -> None:
        self.clientAPI = APIClient()
        self.user = User.objects.create(
            username="teste", password="teste", is_superuser=True
        )
        self.dados_corretos = {"conta_origem": 1, "conta_destino": 3, "valor": 5.0}
        self.dados_errados = {"conta_origem": 3, "conta_destino": 3, "valor": 10}

    def test_verifica_carregamento_da_fixture(self):
        """Checando dados gerados na fixture"""
        primeira_transacao = Transacao.objects.get(id=1)
        todas_transacoes = Transacao.objects.all()
        self.assertEqual(str(primeira_transacao.data_transacao), "2022-07-16")
        self.assertEqual(len(todas_transacoes), 9)

    def test_de_autorizacao_negada(self):
        """Tentativa de acesso sem autenticar usuario"""
        # dado
        transacao = self.dados_corretos

        # quando
        response = self.clientAPI.post("/criartransacao/", transacao, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_transacao_post(self):
        """Tentativa de POST com dados corretos"""
        # dado
        transacao = self.dados_corretos
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.post("/criartransacao/", transacao, format="json")
        objeto_gerado = Transacao.objects.get(id=10)

        # entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(objeto_gerado.conta_origem, transacao["conta_origem"])
        self.assertEqual(objeto_gerado.conta_destino, transacao["conta_destino"])
        self.assertEqual(objeto_gerado.valor, transacao["valor"])

    def test_transacao_post_errado(self):
        """Tentativa de POST com dados errados"""
        # dado
        transacao = self.dados_errados
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.post("/criartransacao/", transacao, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transacao_get(self):
        """Tentativa de GET com dados corretos"""
        # dado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.get("/criartransacao/")

        # entao
        self.assertEqual(response.status_code, status.HTTP_200_OK)
