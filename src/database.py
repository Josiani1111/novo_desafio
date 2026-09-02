import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("clientes.db")
    return conexao


def criar_tabela():
    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_tabela()
    print("Tabela clientes criada com sucesso!")