from ..Cadastrar.criarConexao import criarConexao, database

def buscarPartidas(modalidade, classificacao):
    conexao = criarConexao()
    
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.partidas')
    partidasBuscadas = cursor.fetchall()

    cursor.close()
    conexao.close()
    return partidasBuscadas

