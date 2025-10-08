from flask import redirect, url_for

from app import app# Rota raiz redireciona para autenticação
@app.route('/')
def index():
	return redirect(url_for('login'))

from app.controller import controle_usuario
from app import app

@app.route('/usuario/autenticacao', methods=['GET', 'POST'])
def login():
	return controle_usuario.login()

@app.route('/usuario/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
	return controle_usuario.cadastro_usuario()

@app.route('/usuario/logout')
def logout():
	return controle_usuario.logout()


