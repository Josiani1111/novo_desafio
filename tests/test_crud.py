import sqlite3
import unittest


class TestCRUD(unittest.TestCase):

    def test_cadastrar_cliente(self):

        conexao = sqlite3.connect(":memory:")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)",
            ("Maria", 50, "Franca")
        )

        conexao.commit()

        cursor.execute("SELECT * FROM clientes")

        resultado = cursor.fetchall()

        self.assertEqual(resultado[0][1], "Maria")
        self.assertEqual(resultado[0][2], 50)
        self.assertEqual(resultado[0][3], "Franca")

        conexao.close()

    def test_listar_cliente(self):

        conexao = sqlite3.connect(":memory:")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)",
            ("Joao", 40, "Ribeirao Preto")
        )

        conexao.commit()

        cursor.execute("SELECT * FROM clientes")

        resultado = cursor.fetchall()

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Joao")

        conexao.close()

    def test_atualizar_cliente(self):

        conexao = sqlite3.connect(":memory:")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)",
            ("Maria", 50, "Franca")
        )

        conexao.commit()

        cursor.execute(
            "UPDATE clientes SET idade = ?, cidade = ? WHERE id = ?",
            (55, "Ribeirao Preto", 1)
        )

        conexao.commit()

        cursor.execute("SELECT * FROM clientes WHERE id = 1")

        resultado = cursor.fetchone()

        self.assertEqual(resultado[2], 55)
        self.assertEqual(resultado[3], "Ribeirao Preto")

        conexao.close()

    def test_excluir_cliente(self):

        conexao = sqlite3.connect(":memory:")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)",
            ("Maria", 50, "Franca")
        )

        conexao.commit()

        cursor.execute(
            "DELETE FROM clientes WHERE id = ?",
            (1,)
        )

        conexao.commit()

        cursor.execute("SELECT * FROM clientes")

        resultado = cursor.fetchall()

        self.assertEqual(resultado, [])

        conexao.close()


if __name__ == "__main__":
    unittest.main()