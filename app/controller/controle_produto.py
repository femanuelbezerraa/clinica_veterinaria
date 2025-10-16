from flask import render_template, request, redirect, url_for, session
from app.models.produto import Produto
from app.models.movimentacao import Movimentacao

def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])
        quantidade_min = int(request.form['quantidade_min'])
        tipo = request.form.get('tipo', '').strip().lower()
        # Validar/normalizar para os valores permitidos na constraint do DB
        allowed = {'comprimido', 'alimento', 'gota'}
        if tipo not in allowed:
            tipo = 'alimento'  # default seguro
        especie = request.form.get('especie')
        dosagem = request.form.get('dosagem')
        validade = request.form.get('validade')

        
        existente = Produto.buscar_por_nome(nome)
        if existente:
            Produto.atualizar_quantidade(
                existente['id_produto'], 
                existente['quantidade'] + quantidade, 
                quantidade_min
            )
            produto_id = existente['id_produto']
        else:
            produto_id = Produto.criar(nome, descricao, quantidade, preco, quantidade_min, tipo, especie, dosagem, validade)

        Movimentacao.registrar_entrada(produto_id, quantidade, session['usuario_id'])
        return redirect(url_for('cadastro_produto'))

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
                Produto.buscar_por_id(produto_id)['quantidade_min']
            )
            Movimentacao.registrar_saida(produto_id, quantidade_saida, session['usuario_id'])
    return redirect(url_for('cadastro_produto'))


def editar_produto(produto_id):
    produto = Produto.buscar_por_id(produto_id)
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        if preco is not None and preco != '':
            try:
                preco = float(preco)
            except ValueError:
                preco = None
        else:
            preco = None

        quantidade_min = request.form.get('quantidade_min')
        if quantidade_min is not None and quantidade_min != '':
            try:
                quantidade_min = int(quantidade_min)
            except ValueError:
                quantidade_min = None
        else:
            quantidade_min = None

        tipo = request.form.get('tipo')
        if tipo:
            tipo = tipo.strip().lower()
            allowed = {'comprimido', 'alimento', 'gota'}
            if tipo not in allowed:
                tipo = 'alimento'

        especie = request.form.get('especie')
        dosagem = request.form.get('dosagem')
        validade = request.form.get('validade') or None

        Produto.atualizar(produto_id, nome=nome, descricao=descricao, preco=preco, quantidade_min=quantidade_min, tipo=tipo, especie=especie, dosagem=dosagem, validade=validade)
        return redirect(url_for('cadastro_produto'))

    return render_template('editar_produto.html', produto=produto, usuario=session.get('usuario_nome'))


def remover_produto(produto_id):
    sucesso = Produto.remover(produto_id)
    if not sucesso:
        # Não é possível remover produto referenciado em movimentações
        return render_template('cadastro_produto.html', produtos=Produto.listar_todos(), usuario=session.get('usuario_nome'), error='Não é possível remover produto que possui movimentações registradas.')
    return redirect(url_for('cadastro_produto'))


def adicionar_quantidade(produto_id):
    if request.method == 'POST':
        q = int(request.form.get('quantidade_adicionar', 0))
        produto = Produto.buscar_por_id(produto_id)
        Produto.atualizar_quantidade(produto_id, produto['quantidade'] + q, produto['quantidade_min'])
        Movimentacao.registrar_entrada(produto_id, q, session['usuario_id'])
    return redirect(url_for('cadastro_produto'))


def retirar_quantidade(produto_id):
    if request.method == 'POST':
        q = int(request.form.get('quantidade_retirar', 0))
        produto = Produto.buscar_por_id(produto_id)
        if produto and produto['quantidade'] >= q:
            Produto.atualizar_quantidade(produto_id, produto['quantidade'] - q, produto['quantidade_min'])
            Movimentacao.registrar_saida(produto_id, q, session['usuario_id'])
    return redirect(url_for('cadastro_produto'))


