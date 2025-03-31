# Catálogo de Produtos Flask

Este é um projeto simples de catálogo de produtos desenvolvido com o framework Flask (Python). Ele permite listar, adicionar, editar e deletar produtos de um banco de dados SQLite.

## Funcionalidades

* **Listagem de Produtos:** Exibe todos os produtos cadastrados com nome, código, descrição e preço.
* **Criação de Produtos:** Permite adicionar novos produtos ao catálogo.
* **Edição de Produtos:** Permite modificar os dados de um produto existente.
* **Exclusão de Produtos:** Permite remover produtos do catálogo.

## Tecnologias Utilizadas

* **Flask:** Framework web Python.
* **SQLite:** Banco de dados relacional leve.
* **Bootstrap:** Framework CSS para estilização da interface.

## Pré-requisitos

* Python 3.x instalado.
* Pip (gerenciador de pacotes do Python) instalado.

## Como Executar o Projeto

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/seu_usuario/catalogo_produtos_flask.git](https://github.com/seu_usuario/catalogo_produtos_flask.git)
    cd catalogo_produtos_flask
    ```

2.  **Criar e ativar um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instalar as dependências:**

    ```bash
    pip install Flask
    ```

4.  **Executar a aplicação:**

    ```bash
    python app.py
    ```

5.  **Acessar no navegador:**

    Abra o seu navegador e acesse `http://127.0.0.1:5000/`.

## Próximos Passos (Ideias para o Futuro)

* Adicionar validação mais robusta aos formulários.
* Implementar busca de produtos.
* Adicionar paginação à listagem de produtos.
* Melhorar a interface do usuário.
* Adicionar testes automatizados.
