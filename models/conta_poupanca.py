from .conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo=0, taxa_rendimento=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not 0 <= valor <= 1
        ):
            raise ValueError("Taxa inválida.")

        self._taxa_rendimento = valor

    def calcular_rendimento(self):
        return round(self.saldo * self.taxa_rendimento, 2)

    def aplicar_rendimento(self):
        rendimento = self.calcular_rendimento()
        self.depositar(rendimento)
        return rendimento

    def __str__(self):
        return (
            f"Conta Poupança | Número: {self.numero} | "
            f"Titular: {self.titular.nome} | "
            f"Saldo: R$ {self.saldo:.2f} | "
            f"Rendimento: {self.taxa_rendimento * 100:.1f}%"
        )

    def __repr__(self):
        return f"ContaPoupanca({self.numero!r}, {self.titular!r}, {self.saldo!r}, {self.taxa_rendimento!r})"