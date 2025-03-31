import sqlite3

DB_NAME = 'produtos.db'


# cria tabela produtos no banco de dados, se não existir
def criar_tabela():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo TEXT UNIQUE NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL
    )
    """)
    # Salva as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Garante que a função 'criar_tabela()'
# seja executada apenas quando o arquivo
# 'db.py' for rodado diretamente
    if __name__ == '__main__':
        criar_tabela()
        print(f"Tabela 'produtos' criada no banco de dados '{DB_NAME}'!")


def obter_conexao():
    # obtém conexão com o banco de dados
    return sqlite3.connect(DB_NAME)


def listar_produtos_db():
    # lista todos os produtos do banco de dados
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "SELECT id, nome, codigo, descricao, preco FROM produtos")
            produtos = cursor.fetchall()
            return produtos
        except sqlite3.Error as e:
            print(f"Erro ao listar produtos: {e}")
            return None


def inserir_produto_db(nome, codigo, descricao, preco):
    # insere novo produto no banco de dados
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos(nome, codigo, descricao, preco) " \
            "VALUES (?, ?, ?, ?)"
        try:
            cursor.execute(sql, (nome, codigo, descricao, preco))
            conexao.commit()
            return True  # inidica sucesso
        except sqlite3.Error as e:
            print(f"Erro ao inserir produto: {e}")
            conexao.rollback()  # desfaz qualquer alteração pendente
            return False  # indica falha


def obter_produto_db(id_produto):
    # obtém os dados de um produto específico do banco de dados
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "SELECT id, nome, codigo, descricao, preco "
                "FROM produtos WHERE id = ?", (id_produto,))
            produto = cursor.fetchone()
            return produto
        except sqlite3.Error as e:
            print(f"Erro ao obter produto: {e}")
            return None


def atualizar_produto_db(id_produto, nome, codigo, descricao, preco):
    # atualiza os dados do produto existente no banco de dados
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        sql = "UPDATE produtos SET nome=?, codigo=?, descricao=?, preco=? " \
            "WHERE id=?"
        try:
            cursor.execute(sql, (nome, codigo, descricao, preco, id_produto))
            conexao.commit()
            return True  # indica sucesso
        except sqlite3.Error as e:
            print(f"Erro ao atualizar produto: {e}")
            conexao.rollback()
            return False  # indica falha


def deletar_produto_db(id_produto):
    # deleta produto do banco de dados
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM produtos WHERE id = ?"
        try:
            cursor.execute(sql, (id_produto,))
            conexao.commit()
            return True  # indica sucesso
        except sqlite3.Error as e:
            print(f"Erro ao deletar produto: {e}")
            conexao.rollback()
            return False  # indica falha
