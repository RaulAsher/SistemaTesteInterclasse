from ..Cadastrar.criarConexao import criarConexao


def buscarEstatisticasDasPartidas(fk_partida):
    conexao = None
    cursor = None

    try:
        conexao = criarConexao()
        cursor = conexao.cursor(dictionary=True)

        query = """
            SELECT *
            FROM estatisticas_partida
            WHERE fk_partida = %s
        """

        cursor.execute(query, (fk_partida,))

        return cursor.fetchall()

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()