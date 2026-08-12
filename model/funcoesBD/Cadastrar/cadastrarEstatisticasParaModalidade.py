from .criarConexao import criarConexao, database

def cadastrarEstatisticasParaModalidade(esporte,estatistica,principal):
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute(f'INSERT INTO estatisticas_esporte (fk_esporte, fk_nome_estatistica, estatistica_principal) values (%s,%s, %s)', (esporte, estatistica,principal))
    conexao.commit()

    cursor.close()
    conexao.close()

    return print('Cadastrado com sucesso')