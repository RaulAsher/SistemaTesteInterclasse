from ..Cadastrar.criarConexao import criarConexao, database

def buscarEstatisticasDasPartidas(fk_partida):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    query = 'SELECT * FROM estatisticas_partida where fk_partida = %s'
    cursor.execute(query, (fk_partida, ))

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    