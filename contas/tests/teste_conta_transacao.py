from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from contas.models.transacao import Transacao


class ContaTestCase(TestCase):

    fixtures = ["db_para_testes"]

    def setUp(self) -> None:
        self.clientAPI = APIClient()
        self.user = User.objects.create(
            username="teste", password="teste", is_superuser=True
        )

    def test_verifica_carregamento_da_fixture(self):
        """Checando dados gerados na fixture"""
        primeira_transacao = Transacao.objects.get(id=1)
        todas_transacoes = Transacao.objects.all()
        self.assertEqual(str(primeira_transacao.data_transacao), "2022-07-16")
        self.assertEqual(len(todas_transacoes), 9)

    def test_filtro_transacao(self):
        """Tentativa de GET das transacoes de uma conta"""
        # dado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response = self.clientAPI.get("/conta/transacao/?conta=1")

        # entao
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filtro_transacao(self):
        """Tentativa de GET das transacoes de uma conta"""
        # dado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response_a = self.clientAPI.get("/conta/transacao/?conta=1")
        response_b = self.clientAPI.get(
            "/conta/transacao/?conta=1&data_inicial=2022-07-12&data_final=2022-07-14"
        )

        # entao
        self.assertEqual(response_a.status_code, status.HTTP_200_OK)
        self.assertEqual(response_b.status_code, status.HTTP_200_OK)

    def test_filtro_transacao_dados(self):
        """Tentativa de GET das transacoes de uma conta com check dos dados"""
        # dado
        self.clientAPI.force_authenticate(user=self.user)

        # quando
        response_a = self.clientAPI.get("/conta/transacao/")
        response_b = self.clientAPI.get("/conta/transacao/?conta=1")
        response_c = self.clientAPI.get(
            "/conta/transacao/?conta=1&data_inicial=2022-07-10&data_final=2022-07-10"
        )

        # entao
        self.assertEqual(len(response_a.data["results"]), 9)
        self.assertEqual(len(response_b.data["results"]), 5)
        self.assertEqual(len(response_c.data["results"]), 1)
