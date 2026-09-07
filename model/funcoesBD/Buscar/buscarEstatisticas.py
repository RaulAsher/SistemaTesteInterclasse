from ..Cadastrar.criarConexao import criarConexao, database


def buscarEstatisticas():
    conexao = None
    cursor = None

    try:
        conexao = criarConexao()
        cursor = conexao.cursor(dictionary=True)

        query = f"""
            SELECT *
            FROM {database}.tipo_estatistica
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()