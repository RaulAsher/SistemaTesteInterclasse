from ..Cadastrar.criarConexao import criarConexao, database


def buscarEsportePorId(pk_esporte):
    conn = None
    cursor = None

    try:
        conn = criarConexao()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT pk_esporte, qtd_jogadores
            FROM esportes
            WHERE pk_esporte = %s
        """

        cursor.execute(query, (pk_esporte,))
        esporte = cursor.fetchone()

        return esporte

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()