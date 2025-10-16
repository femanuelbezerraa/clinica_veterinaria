from app.database.db import query_db, execute_db

class Movimentacao:
    @staticmethod
    def registrar_entrada(produto_id, quantidade, usuario_id):
        execute_db(
            'INSERT INTO movimentacao (produto_id, tipo_movimentacao, quantidade, usuario_id, data_movimentacao) VALUES (%s,%s,%s,%s, NOW())',
            (produto_id, 'Entrada', quantidade, usuario_id)
        )

    @staticmethod
    def registrar_saida(produto_id, quantidade, usuario_id):
        execute_db(
            'INSERT INTO movimentacao (produto_id, tipo_movimentacao, quantidade, usuario_id, data_movimentacao) VALUES (%s,%s,%s,%s, NOW())',
            (produto_id, 'Saida', quantidade, usuario_id)
        )

    @staticmethod
    def listar_todas():
        return query_db('''
            SELECT m.id_movimentacao AS id, m.produto_id, p.nome AS nome_produto, m.tipo_movimentacao, m.quantidade, m.data_movimentacao, u.nome AS usuario_nome, m.usuario_id AS usuario_id
            FROM movimentacao AS m
            JOIN produto AS p ON m.produto_id = p.id_produto
            JOIN usuario AS u ON m.usuario_id = u.id_usuario
            ORDER BY m.data_movimentacao DESC
        ''')


