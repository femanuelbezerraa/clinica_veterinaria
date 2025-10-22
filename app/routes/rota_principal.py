from flask import Blueprint, render_template, session, redirect, url_for
from app import app
from app.controller import controle_usuario

principal_bp = Blueprint("principal", __name__)

@principal_bp.route("/principal")
def principal():
    if "usuario" not in session:
        return redirect(url_for("login.login"))
    return controle_usuario.tela_principal()

@app.route('/principal')
def tela_principal():
    return controle_usuario.tela_principal()
