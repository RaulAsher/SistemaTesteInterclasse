from ..Cadastrar.criarConexao import criarConexao


def buscarEsportePorPartida(pk_partida):
    conexao = None
    cursor = None

    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        query = """
            SELECT fk_esporte
            FROM partidas
            WHERE pk_partida = %s
        """

        cursor.execute(query, (pk_partida,))
        esporte = cursor.fetchone()

        if esporte is None:
            return None

        return esporte[0]

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()