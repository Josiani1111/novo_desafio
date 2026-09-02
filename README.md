# Sistema de Clientes

Sistema de cadastro de clientes desenvolvido em Python com banco de dados SQLite, utilizando operações CRUD, validação de dados e testes automatizados.

## 📌 Sobre o projeto

Este projeto foi desenvolvido para praticar conceitos fundamentais de desenvolvimento de sistemas, incluindo programação em Python, banco de dados SQLite, operações SQL, organização de código e testes automatizados.

O sistema permite cadastrar, consultar, atualizar e excluir clientes por meio de um menu interativo no terminal.

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
* Unittest
* Git
* GitHub

## 🧪 Testes automatizados

O projeto possui testes utilizando `unittest`.

Atualmente são **12 testes automatizados**, cobrindo validações e operações CRUD.

Resultado:

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

No Windows, abra o PowerShell dentro da pasta do projeto e execute:

```powershell
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

Para executar todos os 12 testes:

```powershell
py -m unittest tests.test_main tests.test_crud
```

O resultado esperado é:

```text
Ran 12 tests

OK
```

## 🎯 Conhecimentos praticados

* Python
* Lógica de programação
* Funções
* Estruturas de repetição
* `try/except`
* Validação de dados
* SQL
* SQLite
* CRUD
* Testes automatizados
* Organização de código
* Git e GitHub

## 👩‍💻 Objetivo profissional

Projeto desenvolvido como parte da minha jornada de aprendizado em Desenvolvimento de Sistemas, com foco em Python, SQL, banco de dados, testes e boas práticas de programação.

