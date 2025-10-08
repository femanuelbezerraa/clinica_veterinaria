from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import Usuario

def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if not Usuario.buscar_por_email(email):
            return render_template('autenticacao.html', erro='Usuário inexistente')

        if check_password_hash(Usuario.buscar_por_email(email)['senha'], senha):
            session['usuario_id'] = Usuario.buscar_por_email(email)['id']
            session['usuario_nome'] = Usuario.buscar_por_email(email)['nome']
            return redirect(url_for('produto.cadastro_produto'))
        else:
            return render_template('autenticacao.html', erro='Senha incorreta')

    return render_template('autenticacao.html')


def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if Usuario.buscar_por_email(email):
            return render_template('cadastro_usuario.html', erro='E-mail já cadastrado')

        senha_hash = generate_password_hash(senha)
        Usuario.criar(nome, email, senha_hash)
        return redirect(url_for('usuario.login'))

    return render_template('cadastro_usuario.html')


def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('usuario.login'))


