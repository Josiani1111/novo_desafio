from database import criar_tabela
from cliente import (
    cadastrar_cliente,
    listar_clientes,
    atualizar_cliente,
    excluir_cliente
)


def menu():
    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            atualizar_cliente()

        elif opcao == "4":
            excluir_cliente()

        elif opcao == "5":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida! Digite uma opção de 1 a 5.")


if __name__ == "__main__":
    criar_tabela()
    menu()