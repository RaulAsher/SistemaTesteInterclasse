from ..Cadastrar.criarConexao import criarConexao


def cadastrarProvaAtletismo(
    fk_modalidade,
    fk_genero,
    nome_prova,
    tipo_resultado,
    unidade_medida,
    data_prova
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
            data_prova,
            status
        )
        VALUES (%s, %s, %s, %s, %s, %s, 'nao_iniciada')
    """

    valores = (
        fk_modalidade,
        fk_genero,
        nome_prova,
        tipo_resultado,
        unidade_medida,
        data_prova
    )

    cursor.execute(query, valores)

    conexao.commit()

    cursor.close()
    conexao.close()