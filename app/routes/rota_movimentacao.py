
from app.controller import controle_movimentacao
from app.decorador import login_required
from app import app

@app.route('/movimentacao/entrada/<int:produto_id>', methods=['POST'])
@login_required
def entrada_produto(produto_id):
    return controle_movimentacao.entrada_produto(produto_id)

@app.route('/movimentacao/saida/<int:produto_id>', methods=['POST'])
@login_required
def saida_produto(produto_id):
    return controle_movimentacao.saida_produto(produto_id)

@app.route('/movimentacao/historico')
@login_required
def historico_estoque():
    return controle_movimentacao.historico_estoque()


