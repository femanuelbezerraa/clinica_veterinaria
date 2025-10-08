from app.controller import controle_produto
from app.decorador import login_required
from app import app

@app.route('/produto/cadastro_produto', methods=['GET', 'POST'])
@login_required
def cadastro_produto():
    return controle_produto.cadastro_produto()
