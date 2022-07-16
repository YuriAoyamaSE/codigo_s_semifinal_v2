from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from contas.models.conta import Conta


class ContaTestCase(TestCase):

    fixtures = ["db_para_testes"]

    def setUp(self) -> None:
        self.clientAPI = APIClient()
        self.user = User.objects.create(
            username="teste", password="teste", is_superuser=True
        )
        self.dados_conta_corretos = {"cliente": "Testador Teste", "saldo": 5.0}
        self.saldo_errado = {"cliente": "Testador Teste", "saldo": -50}
        self.cliente_errado = {"cliente": "123", "saldo": 5.0}

    def test_verifica_carregamento_da_fixture(self):
        """Checando dados gerados na fixture"""
        primeira_conta = Conta.objects.get(id=1)
        todas_contas = Conta.objects.all()
        self.assertEqual(primeira_conta.cliente, "cliente dez")
        self.assertEqual(len(todas_contas), 3)

    def test_de_autorizacao_negada(self):
        """Tentativa de acesso sem autenticar usuario"""
        # dado
        conta = self.dados_conta_corretos

        # quando
        response = self.clientAPI.post("/criarconta/", conta, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_conta_post(self):
        """Tentativa de POST com dados corretos"""
        # dado
        conta = self.dados_conta_corretos
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.post("/criarconta/", conta, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Conta.objects.get(cliente=conta["cliente"]).saldo, conta["saldo"]
        )

    def test_conta_post_erro_saldo(self):
        """Tentativa de POST com saldo negativo"""
        # dado
        conta = self.saldo_errado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.post("/criarconta/", conta, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_conta_post_erro_cliente(self):
        """Tentativa de POST com nome numerico"""
        # dado
        conta = self.cliente_errado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.post("/criarconta/", conta, format="json")

        # entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_conta_get(self):
        """Tentativa de GET das contas"""
        # dado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.get("/criarconta/")

        # entao
        self.assertEqual(response.status_code, status.HTTP_200_OK)
