# 👥 Sistema de Clientes

Sistema de cadastro e gerenciamento de clientes desenvolvido em **Python**, utilizando **SQLite**, operações **CRUD**, validação de dados e testes automatizados.

## 📌 Sobre o projeto

Este projeto foi desenvolvido para praticar conceitos fundamentais de desenvolvimento de sistemas, incluindo programação em Python, banco de dados SQLite, operações SQL, organização de código, tratamento de erros e testes automatizados.

O sistema permite **cadastrar, listar, atualizar e excluir clientes** por meio de um menu interativo no terminal.

## 🚀 Funcionalidades

* Cadastro de clientes
* Listagem de clientes
* Atualização de clientes
* Exclusão de clientes
* Validação de nome, idade, ID e cidade
* Tratamento de erros de entrada
* Banco de dados SQLite
* Criação automática da tabela de clientes
* Confirmação antes da exclusão

## 🛠️ Tecnologias utilizadas

* Python
* SQLite
* SQL
* `unittest`
* Git
* GitHub

## 🧪 Testes automatizados

O projeto possui testes automatizados desenvolvidos com **`unittest`**.

Atualmente, o projeto possui **12 testes automatizados**, abrangendo validações e operações CRUD.

Resultado dos testes:

```text
Ran 12 tests

OK
```

## 📁 Estrutura do projeto

```text
novo_desafio/
│
├── .gitignore
├── README.md
│
├── src/
│   ├── cliente.py
│   ├── database.py
│   ├── main.py
│   ├── utils.py
│   └── __init__.py
│
└── tests/
    ├── test_crud.py
    └── test_main.py
```

## ▶️ Como executar

No Windows, abra o **PowerShell** dentro da pasta do projeto e execute:

```text
py src\main.py
```

O sistema apresentará o menu:

```text
===== SISTEMA DE CLIENTES =====
1 - Cadastrar cliente
2 - Listar clientes
3 - Atualizar cliente
4 - Excluir cliente
5 - Sair
```

## 🧪 Como executar os testes

Para executar os 12 testes automatizados:

```text
py -m unittest tests.test_main tests.test_crud
```

Resultado esperado:

```text
Ran 12 tests

OK
```

## 🎯 Conhecimentos praticados

* Python
* Lógica de programação
* Funções
* Estruturas de repetição
* Estruturas condicionais
* Tratamento de exceções com `try/except`
* Validação de dados
* SQL
* SQLite
* Operações CRUD
* Testes automatizados
* Organização de código
* Git e GitHub

## 👩‍💻 Objetivo profissional

Este projeto faz parte da minha jornada de aprendizado em **Análise e Desenvolvimento de Sistemas**, com foco no desenvolvimento de aplicações utilizando Python, banco de dados, SQL e testes automatizados.

Através deste projeto, busquei colocar em prática conceitos de programação, organização de código, validação, tratamento de erros e testes.

---

**Josiani Oliveira**

[GitHub — @Josiani1111](https://github.com/Josiani1111)
