from ..Cadastrar.criarConexao import criarConexao, database


def deletarModalidadeAtletismo(pk_modalidade):
    conexao = criarConexao()

    try:
        with conexao.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM modalidades_atletismo
                WHERE pk_modalidade = %s
                """,
                (pk_modalidade,)
            )

        conexao.commit()

    finally:
        conexao.close()