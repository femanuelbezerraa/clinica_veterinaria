from app.controller import controle_produto
from app.decorador import login_required
from app import app

@app.route('/produto/cadastro_produto', methods=['GET', 'POST'])
@login_required
def cadastro_produto():
    return controle_produto.cadastro_produto()


@app.route('/produto/editar/<int:produto_id>', methods=['GET', 'POST'])
@login_required
def editar_produto(produto_id):
    return controle_produto.editar_produto(produto_id)


@app.route('/produto/remover/<int:produto_id>', methods=['POST'])
@login_required
def remover_produto(produto_id):
    return controle_produto.remover_produto(produto_id)


@app.route('/produto/adicionar_quantidade/<int:produto_id>', methods=['POST'])
@login_required
def adicionar_quantidade(produto_id):
    return controle_produto.adicionar_quantidade(produto_id)


@app.route('/produto/retirar_quantidade/<int:produto_id>', methods=['POST'])
@login_required
def retirar_quantidade(produto_id):
    return controle_produto.retirar_quantidade(produto_id)
