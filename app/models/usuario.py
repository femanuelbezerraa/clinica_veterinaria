from app.database.db import query_db, execute_db

class Usuario:
    @staticmethod
    def buscar_por_email(email):
        return query_db('SELECT * FROM usuarios WHERE email=%s', (email,), one=True)

    @staticmethod
    def buscar_por_id(usuario_id):
        return query_db('SELECT * FROM usuarios WHERE id=%s', (usuario_id,), one=True)

    @staticmethod
    def criar(nome, email, senha_hash):
        execute_db('INSERT INTO usuarios (nome, email, senha) VALUES (%s,%s,%s)', 
                   (nome, email, senha_hash))
