from ..Cadastrar.criarConexao import criarConexao, database

def buscarEsportePorPartida(pk_partida,):
    conn = criarConexao()
    cursor = conn.cursor()
    query = """    
    SELECT fk_esporte 
    from partidas 
    where pk_partida = %s;
    """
    cursor.execute(query, (pk_partida,))
    esporte = cursor.fetchone()
    cursor.close()
    conn.close()
    return esporte