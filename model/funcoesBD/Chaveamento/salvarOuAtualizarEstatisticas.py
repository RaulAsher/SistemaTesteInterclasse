from ..Cadastrar.criarConexao import criarConexao

def salvarOuAtualizarEstatistica(
    id_partida,
    nome_estatistica,
    valor_time_casa,
    valor_time_visitante
):
    conexao = criarConexao()
    cursor = conexao.cursor()

    # Verifica se já existe
    query_verificar = '''
        SELECT 1
        FROM estatisticas_partida
        WHERE fk_partida = %s
        AND fk_nome_estatistica = %s
    '''

    cursor.execute(query_verificar, (
        id_partida,
        nome_estatistica
    ))

    existe = cursor.fetchone()

    if existe:
        # Já existe -> UPDATE
        query = '''
            UPDATE estatisticas_partida
            SET valor_time_casa = %s,
                valor_time_visitante = %s
            WHERE fk_partida = %s
            AND fk_nome_estatistica = %s
        '''

        cursor.execute(query, (
            valor_time_casa,
            valor_time_visitante,
            id_partida,
            nome_estatistica
        ))

        print(">>> UPDATE:", nome_estatistica)

    else:
        # Não existe -> INSERT
        query = '''
            INSERT INTO estatisticas_partida(
                fk_partida,
                fk_nome_estatistica,
                valor_time_casa,
                valor_time_visitante
            )
            VALUES (%s, %s, %s, %s)
        '''

        cursor.execute(query, (
            id_partida,
            nome_estatistica,
            valor_time_casa,
            valor_time_visitante
        ))

        print(">>> INSERT:", nome_estatistica)

    conexao.commit()

    cursor.close()
    conexao.close()