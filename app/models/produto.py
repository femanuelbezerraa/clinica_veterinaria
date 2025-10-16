from app.database.db import query_db, execute_db

class Produto:
    @staticmethod
    def listar_todos():
        return query_db('SELECT * FROM produto ORDER BY quantidade - quantidade_min')

    @staticmethod
    def buscar_por_nome(nome):
        return query_db('SELECT * FROM produto WHERE nome=%s', (nome,), one=True)

    @staticmethod
    def buscar_por_id(produto_id):
        return query_db('SELECT * FROM produto WHERE id_produto=%s', (produto_id,), one=True)

    @staticmethod
    def criar(nome, descricao, quantidade, preco, quantidade_min, tipo=None, especie=None, dosagem=None, validade=None, fornecedor_id=None):
        return execute_db('''INSERT INTO produto (nome, descricao, quantidade, preco, quantidade_min, tipo, especie, dosagem, validade, fornecedor_id)
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id_produto''',
                          (nome, descricao, quantidade, preco, quantidade_min, tipo, especie, dosagem, validade, fornecedor_id))

    @staticmethod
    def atualizar_quantidade(produto_id, quantidade, quantidade_min):
        execute_db('UPDATE produto SET quantidade=%s, quantidade_min=%s WHERE id_produto=%s', (quantidade, quantidade_min, produto_id))

    @staticmethod
    def atualizar(produto_id, nome=None, descricao=None, quantidade=None, preco=None, quantidade_min=None, tipo=None, especie=None, dosagem=None, validade=None, fornecedor_id=None):
        # Monta dinamicamente a query de update com os campos fornecidos
        campos = []
        valores = []
        if nome is not None:
            campos.append('nome=%s'); valores.append(nome)
        if descricao is not None:
            campos.append('descricao=%s'); valores.append(descricao)
        if quantidade is not None:
            campos.append('quantidade=%s'); valores.append(quantidade)
        if preco is not None:
            campos.append('preco=%s'); valores.append(preco)
        if quantidade_min is not None:
            campos.append('quantidade_min=%s'); valores.append(quantidade_min)
        if tipo is not None:
            campos.append('tipo=%s'); valores.append(tipo)
        if especie is not None:
            campos.append('especie=%s'); valores.append(especie)
        if dosagem is not None:
            campos.append('dosagem=%s'); valores.append(dosagem)
        if validade is not None:
            campos.append('validade=%s'); valores.append(validade)
        if fornecedor_id is not None:
            campos.append('fornecedor_id=%s'); valores.append(fornecedor_id)

        if not campos:
            return None

        set_clause = ', '.join(campos)
        valores.append(produto_id)
        execute_db(f'UPDATE produto SET {set_clause} WHERE id_produto=%s', tuple(valores))

    @staticmethod
    def remover(produto_id):
        # Verifica se existem movimentações referenciando este produto
        # Na tabela movimentacao a coluna que referencia produto é 'produto_id'
        referencia = query_db('SELECT 1 FROM movimentacao WHERE produto_id=%s LIMIT 1', (produto_id,), one=True)
        if referencia:
            # Não permite exclusão quando há registros de movimentação
            return False
        execute_db('DELETE FROM produto WHERE id_produto=%s', (produto_id,))
        return True


