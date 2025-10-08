from app.database.db import query_db, execute_db

class Produto:
    @staticmethod
    def listar_todos():
        return query_db('SELECT * FROM produtos ORDER BY quantidade - quantidade_minima')

    @staticmethod
    def buscar_por_nome(nome):
        return query_db('SELECT * FROM produtos WHERE nome=%s', (nome,), one=True)

    @staticmethod
    def buscar_por_id(produto_id):
        return query_db('SELECT * FROM produtos WHERE id=%s', (produto_id,), one=True)

    @staticmethod
    def criar(nome, descricao, quantidade, preco, quantidade_minima, tipo=None, especie=None, dosagem=None, validade=None, id_fornecedor=None):
        return execute_db('''INSERT INTO produtos (nome, descricao, quantidade, preco, quantidade_minima, tipo, especie, dosagem, validade, id_fornecedor)
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id''',
                          (nome, descricao, quantidade, preco, quantidade_minima, tipo, especie, dosagem, validade, id_fornecedor))

    @staticmethod
    def atualizar_quantidade(produto_id, quantidade, quantidade_minima):
        execute_db('UPDATE produtos SET quantidade=%s, quantidade_minima=%s WHERE id=%s', (quantidade, quantidade_minima, produto_id))


