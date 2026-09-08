from ..Cadastrar.criarConexao import criarConexao, database

def buscarEsporteMonitor(session_nome):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            query = """
                    SELECT fk_esporte from login where pk_usuario = %s
                """
            cursor.execute(query, (session_nome,))
            return cursor.fetchall()[0]
    finally:
        conexao.close()
    