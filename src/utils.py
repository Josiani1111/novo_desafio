def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))

            if 0 <= idade <= 120:
                return idade

            print("Digite uma idade entre 0 e 120!")

        except ValueError:
            print("Digite apenas números!")


def ler_id():
    while True:
        try:
            id_cliente = int(input("Digite o ID do cliente: "))

            if id_cliente > 0:
                return id_cliente

            print("O ID deve ser maior que zero!")

        except ValueError:
            print("Digite apenas números!")


def ler_nome():
    while True:
        nome = input("Digite o nome: ")

        if nome.strip() != "":
            return nome.strip().title()

        print("O nome não pode ficar vazio!")


def ler_cidade():
    while True:
        cidade = input("Digite a cidade: ")

        if cidade.strip() != "":
            return cidade.strip().title()

        print("A cidade não pode ficar vazia!")