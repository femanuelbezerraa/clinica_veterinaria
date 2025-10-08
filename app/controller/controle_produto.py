from flask import render_template, request, redirect, url_for, session
from app.models.produto import Produto
from app.models.movimentacao import Movimentacao

def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])
        quantidade_minima = int(request.form['quantidade_minima'])
        tipo = request.form.get('tipo')
        especie = request.form.get('especie')
        dosagem = request.form.get('dosagem')

        
        if Produto.buscar_por_nome(nome):
            Produto.atualizar_quantidade(
                Produto.buscar_por_nome(nome)['id'], 
                Produto.buscar_por_nome(nome)['quantidade'] + quantidade, 
                quantidade_minima
            )
            produto_id = Produto.buscar_por_nome(nome)['id']
        else:
            produto_id = Produto.criar(nome, descricao, quantidade, preco, quantidade_minima, tipo, especie, dosagem)

        Movimentacao.registrar(produto_id, 'entrada', quantidade, session['usuario_id'])
        return redirect(url_for('produto.cadastro_produto'))

    return render_template(
        'cadastro_produto.html', 
        produtos=Produto.listar_todos(),
        usuario=session.get('usuario_nome')
    )


def saida_produto(produto_id):
    if request.method == 'POST':
        quantidade_saida = int(request.form['quantidade_saida'])
        if Produto.buscar_por_id(produto_id) and quantidade_saida > 0 and Produto.buscar_por_id(produto_id)['quantidade'] >= quantidade_saida:
            Produto.atualizar_quantidade(
                produto_id, 
                Produto.buscar_por_id(produto_id)['quantidade'] - quantidade_saida,
                Produto.buscar_por_id(produto_id)['quantidade_minima']
            )
            Movimentacao.registrar(produto_id, 'saida', quantidade_saida, session['usuario_id'])
    return redirect(url_for('produto.cadastro_produto'))


