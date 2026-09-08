from ..Cadastrar.criarConexao import criarConexao, database


def editarModalidadeAtletismo(
    pk_modalidade,
    nome_modalidade,
    descricao,
    ativo
):
    conn = criarConexao()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE modalidades_atletismo
        SET
            nome_modalidade = %s,
            descricao = %s,
            ativo = %s
        WHERE pk_modalidade = %s
        """,
        (
            nome_modalidade,
            descricao,
            ativo,
            pk_modalidade
        )
    )

    conn.commit()
    conn.close()