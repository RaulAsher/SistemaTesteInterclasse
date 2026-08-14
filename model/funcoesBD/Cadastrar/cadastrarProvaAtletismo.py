from ..Cadastrar.criarConexao import criarConexao


def cadastrarProvaAtletismo(
    fk_modalidade,
    fk_genero,
    nome_prova,
    tipo_resultado,
    unidade_medida,
    data_hora
):

    conexao = criarConexao()
    cursor = conexao.cursor()

    query = """
        INSERT INTO provas_atletismo (
            fk_modalidade,
            fk_genero,
            nome_prova,
            tipo_resultado,
            unidade_medida,
            data_hora,
            ativo
        )
        VALUES (%s, %s, %s, %s, %s, %s, 1)
    """

    valores = (
        fk_modalidade,
        fk_genero,
        nome_prova,
        tipo_resultado,
        unidade_medida,
        data_hora
    )

    cursor.execute(query, valores)

    conexao.commit()

    cursor.close()
    conexao.close()