import re


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome inválido.")

        self._nome = valor.strip().title()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", valor
        ):
            raise ValueError("E-mail inválido.")

        self._email = valor.lower()

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"

    def __repr__(self):
        return f"Cliente({self.nome!r}, {self.email!r})"