from .criarConexao import criarConexao, database

def cadastrarEsportes(esporte, grupo, qtdJogadores):
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute(f'INSERT INTO {database}.esportes (pk_esporte, grupo, qtd_jogadores) values (%s, %s, %s)', (esporte, grupo, qtdJogadores))
    conexao.commit()

    cursor.close()
    conexao.close()

    return print('Cadastrado com sucesso')