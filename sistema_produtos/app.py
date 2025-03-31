# importa classes necessárias do Flask # type: ignore
from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from db_utils import (
    listar_produtos_db, inserir_produto_db, obter_produto_db,
    atualizar_produto_db, deletar_produto_db
)

app = Flask(__name__)  # cria instância do Flask
app.secret_key = 'chave_secreta'
# chave secreta para usar o flash


# define rota para página inicial '(/)'
@app.route('/')
# função a ser executada quando user acessar página inicial
def listar_produtos():
    produtos = listar_produtos_db()
    return render_template('listar_produtos.html', produtos=produtos)


@app.route('/criar', methods=['GET'])
def criar_produto():
    return render_template('criar_produto.html')


def validar_produto(nome, codigo, preco_str):
    # valida dados recebidos do produto do formulário
    if not nome or not codigo or not preco_str:
        return 'Favor preencher todos os campos obrigatórios.'
    try:
        preco = float(preco_str)
        if preco <= 0:
            return 'Preço deve ser valor positivo.'
    except ValueError:
        return 'Favor inserir valor numérico válido para o preço.'
    return None


def processar_resultado_db(
        resultado, msg_sucesso, msg_erro, url_sucesso, url_erro, **kwargs
):
    # processa resultado de operação no banco de dados e exibe msg flash
    if resultado:
        flash(msg_sucesso, 'success')
        return redirect(url_for(url_sucesso, **kwargs))
    else:
        flash(msg_erro, 'error')
        return redirect(url_for(url_erro, **kwargs))


@app.route('/salvar', methods=['POST'])
def salvar_produto():
    nome = request.form.get('nome')
    codigo = request.form.get('codigo')
    descricao = request.form.get('descricao')
    preco_str = request.form.get('preco')

    erro_validacao = validar_produto(
        nome, codigo, preco_str
        )
    if erro_validacao:
        flash(erro_validacao, 'error')
        return redirect(url_for('criar_produto'))
    try:
        preco = float(preco_str)
        return processar_resultado_db(
            inserir_produto_db(nome, codigo, descricao, preco),
            'Produto criado com sucesso!',
            'Erro ao criar produto, tente novamente.',
            'listar_produtos',
            'criar_produto'
        )
    except ValueError:
        flash(
            'Favor inserir valor numérico válido para preço.', 'error'
        )
        return redirect(url_for('criar_produto'))


@app.route('/atualizar/<int:id_produto>', methods=['POST'])
def atualizar_produto(id_produto):
    nome = request.form.get('nome')
    codigo = request.form.get('codigo')
    descricao = request.form.get('descricao')
    preco_str = request.form.get('preco')

    erro_validacao = validar_produto(
        nome, codigo, preco_str
    )
    if erro_validacao:
        flash(erro_validacao, 'error')
        return redirect(url_for(
            'editar_produto', id_produto=id_produto
        ))
    try:
        preco = float(preco_str)
        return processar_resultado_db(
            atualizar_produto_db(
                id_produto, nome, codigo, descricao, preco
            ),
            'Produto atualizado com sucesso!',
            'Erro ao atualizar produto, tente novamente.',
            'listar_produtos',
            'editar_produtos',
            id_produto=id_produto
        )
    except ValueError:
        flash(
            'Favor inserir valor numérico válido para preço.',
            'error'
        )
        return redirect(url_for(
            'editar_produto', id_produto=id_produto
        ))


@app.route('/editar/<int:id_produto>', methods=['GET'])
def editar_produto(id_produto):
    produto = obter_produto_db(id_produto)
    if produto:
        return render_template('editar_produto.html', produto=produto)
    else:
        flash(
            'Produto não encontrado.', 'error'
        )
        return redirect(url_for('listar_produtos'))


@app.route('/deletar/<int:id_produto>')
def deletar_produto(id_produto):
    return processar_resultado_db(
        deletar_produto_db(id_produto),
        'Produto deletado com sucesso!',
        'Erro ao deletar produto, tente novamente.',
        'listar_produtos',
        'editar_produtos'
    )


# inicia DevServer do Flask quando file é executado diretamente
if __name__ == '__main__':
    # 'debug=True' ajuda a ver erros durante o desenvolvimento
    app.run(debug=True)
