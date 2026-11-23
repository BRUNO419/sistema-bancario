import unittest

from models import (
    Cliente,
    ContaCorrente,
    ContaPoupanca
)


class TestSistemaBancario(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Maria Silva", "maria@email.com")

        self.corrente = ContaCorrente(
            "001", self.cliente, 1000
        )

        self.poupanca = ContaPoupanca(
            "002", self.cliente, 1000
        )

    def test_criar_cliente(self):
        self.assertEqual(self.cliente.nome, "Maria Silva")

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("João", "email_invalido")

    def test_depositar(self):
        self.corrente.depositar(500)
        self.assertEqual(self.corrente.saldo, 1500)

    def test_sacar(self):
        self.corrente.sacar(200)
        self.assertEqual(self.corrente.saldo, 800)

    def test_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.corrente.sacar(2000)

    def test_deposito_invalido(self):
        with self.assertRaises(ValueError):
            self.corrente.depositar(-100)

    def test_rendimento_poupanca(self):
        rendimento = self.poupanca.calcular_rendimento()
        self.assertEqual(rendimento, 10)

    def test_rendimento_conta_corrente(self):
        rendimento = self.corrente.calcular_rendimento()
        self.assertEqual(rendimento, 0)

    def test_comparacao_contas(self):
        self.assertNotEqual(self.corrente, self.poupanca)

    def test_tarifa_conta_corrente(self):
        self.corrente.cobrar_tarifa()
        self.assertEqual(self.corrente.saldo, 985)

    def test_taxa_invalida(self):
        with self.assertRaises(ValueError):
            self.poupanca.taxa_rendimento = 2


if __name__ == "__main__":
    unittest.main()