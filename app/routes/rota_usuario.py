from flask import redirect, url_for
from app import app
from app.controller import controle_usuario
from app.controller import controle_principal  # novo import

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/usuario/autenticacao', methods=['GET', 'POST'])
def login():
    return controle_usuario.login()

@app.route('/usuario/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    return controle_usuario.cadastro_usuario()

@app.route('/usuario/logout')
def logout():
    return controle_usuario.logout()

# Rota da tela principal (chama o novo controller)
@app.route('/principal')
def tela_principal():
    return controle_principal.tela_principal()


