from .criarConexao import criarConexao

def salvarDadosEstatisticos(id_partida, nome_estatistica, valor_time_casa, valor_time_visitante):
    conexao = criarConexao()
    cursor = conexao.cursor()

    query = '''
    INSERT INTO estatisticas_partida(fk_partida, fk_nome_estatistica, valor_time_casa, valor_time_visitante) 
    VALUES (%s, %s, %s, %s)
    '''

    cursor.execute(query, (id_partida, nome_estatistica, valor_time_casa, valor_time_visitante))
    conexao.commit()
    
    cursor.close()
    conexao.close()