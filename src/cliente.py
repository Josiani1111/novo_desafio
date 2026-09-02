import sqlite3

from database import conectar_banco
from utils import ler_nome, ler_idade, ler_id, ler_cidade


def cadastrar_cliente():
    print("===== CADASTRO DE CLIENTE =====")

    nome = ler_nome()
    idade = ler_idade()
    cidade = ler_cidade()

    conexao = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)",
            (nome, idade, cidade)
        )

        conexao.commit()

        print("Cliente cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()


def listar_clientes():
    print("===== LISTA DE CLIENTES =====")

    conexao = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, idade, cidade FROM clientes"
        )

        clientes = cursor.fetchall()

        if not clientes:
            print("Nenhum cliente cadastrado.")

        else:
            for cliente in clientes:
                print("ID:", cliente[0])
                print("Nome:", cliente[1])
                print("Idade:", cliente[2])
                print("Cidade:", cliente[3])
                print("--------------------")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()


def atualizar_cliente():
    print("===== ATUALIZAR CLIENTE =====")

    id_cliente = ler_id()
    nome = ler_nome()
    idade = ler_idade()
    cidade = ler_cidade()

    conexao = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE clientes SET nome = ?, idade = ?, cidade = ? WHERE id = ?",
            (nome, idade, cidade, id_cliente)
        )

        quantidade = cursor.rowcount

        conexao.commit()

        if quantidade > 0:
            print("Cliente atualizado com sucesso!")

        else:
            print("Cliente não encontrado!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()


def excluir_cliente():
    print("===== EXCLUIR CLIENTE =====")

    id_cliente = ler_id()

    confirmacao = input(
        "Tem certeza que deseja excluir? (s/n): "
    )

    if confirmacao.lower() != "s":
        print("Exclusão cancelada!")
        return

    conexao = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM clientes WHERE id = ?",
            (id_cliente,)
        )

        quantidade = cursor.rowcount

        conexao.commit()

        if quantidade > 0:
            print("Cliente excluído com sucesso!")

        else:
            print("Cliente não encontrado!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()