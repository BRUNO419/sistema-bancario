from abc import ABC, abstractmethod
import math
from .cliente import Cliente


class Conta(ABC):

    def __init__(self, numero, titular, saldo=0):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("Número da conta inválido.")

        if not isinstance(titular, Cliente):
            raise TypeError("O titular deve ser um Cliente.")

        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor < 0
        ):
            raise ValueError("Saldo inválido.")

        self._saldo = round(float(valor), 2)

    def depositar(self, valor):
        self._validar_valor(valor)
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self._validar_valor(valor)

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= valor
        return self.saldo

    @staticmethod
    def _validar_valor(valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor <= 0
        ):
            raise ValueError("O valor deve ser positivo.")

    @abstractmethod
    def calcular_rendimento(self):
        pass

    def __str__(self):
        return (
            f"Conta: {self.numero} | "
            f"Titular: {self.titular.nome} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numero!r}, {self.titular!r}, {self.saldo!r})"

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.numero == outra.numero

    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo < outra.saldo