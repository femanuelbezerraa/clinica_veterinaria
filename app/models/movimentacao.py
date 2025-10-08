from app.database.db import query_db, execute_db

class Movimentacao:
    @staticmethod
    def registrar_entrada(produto_id, quantidade, usuario_id):
        execute_db(
            'INSERT INTO movimentacao_estoque (produto_id, tipo_movimentacao, quantidade, usuario_id) VALUES (%s,%s,%s,%s)',
            (produto_id, 'entrada', quantidade, usuario_id)
        )

    @staticmethod
    def registrar_saida(produto_id, quantidade, usuario_id):
        execute_db(
            'INSERT INTO movimentacao_estoque (produto_id, tipo_movimentacao, quantidade, usuario_id) VALUES (%s,%s,%s,%s)',
            (produto_id, 'saida', quantidade, usuario_id)
        )

    @staticmethod
    def listar_todas():
        return query_db('''
            SELECT m.id, m.produto_id, p.nome AS nome_produto, m.tipo_movimentacao, m.quantidade, m.data_movimentacao, u.nome AS usuario_nome
            FROM movimentacao_estoque AS m
            JOIN produtos AS p ON m.produto_id = p.id
            JOIN usuarios AS u ON m.usuario_id = u.id
            ORDER BY m.data_movimentacao DESC
        ''')


