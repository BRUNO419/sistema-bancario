from models import Cliente, ContaCorrente, ContaPoupanca


def main():
    print("=" * 50)
    print("       SISTEMA BANCÁRIO")
    print("=" * 50)

    clientes = [
        Cliente("Ana Silva", "ana@email.com"),
        Cliente("Bruno Costa", "bruno@email.com"),
        Cliente("Carla Souza", "carla@email.com"),
        Cliente("Daniel Lima", "daniel@email.com"),
        Cliente("Eduarda Alves", "eduarda@email.com"),
        Cliente("Felipe Santos", "felipe@email.com"),
        Cliente("Gabriela Rocha", "gabriela@email.com"),
        Cliente("Henrique Melo", "henrique@email.com"),
        Cliente("Isabela Martins", "isabela@email.com"),
        Cliente("João Oliveira", "joao@email.com")
    ]

    contas = [
        ContaCorrente("001", clientes[0], 1500),
        ContaPoupanca("002", clientes[1], 2000),
        ContaCorrente("003", clientes[2], 3000),
        ContaPoupanca("004", clientes[3], 2500),
        ContaCorrente("005", clientes[4], 1800),
        ContaPoupanca("006", clientes[5], 4000),
        ContaCorrente("007", clientes[6], 1200),
        ContaPoupanca("008", clientes[7], 3500),
        ContaCorrente("009", clientes[8], 5000),
        ContaPoupanca("010", clientes[9], 4500)
    ]

    print("\n--- CONTAS CADASTRADAS ---")

    for conta in contas:
        print(conta)

    print("\n--- DEMONSTRAÇÃO DE POLIMORFISMO ---")

    for conta in contas:
        rendimento = conta.calcular_rendimento()

        print(
            f"{type(conta).__name__}: "
            f"Rendimento calculado = R$ {rendimento:.2f}"
        )

    print("\n--- OPERAÇÕES ---")

    contas[0].depositar(500)
    print("Depósito realizado na conta 001.")

    contas[1].sacar(200)
    print("Saque realizado na conta 002.")

    print("\n--- TRATAMENTO DE ERROS ---")

    try:
        contas[0].sacar(999999)
    except ValueError as erro:
        print(f"Erro tratado: {erro}")

    try:
        Cliente("Teste", "email_invalido")
    except ValueError as erro:
        print(f"Erro tratado: {erro}")

    print("\n--- CONTAS ORDENADAS POR SALDO ---")

    for conta in sorted(contas):
        print(conta)

    print("\nSistema finalizado!")


if __name__ == "__main__":
    main()