from ..Cadastrar.criarConexao import criarConexao, database

def buscarProvaPorID():

    conexao = criarConexao()

    query = 'SELECT pk_prova FROM provas_atletismo WHERE pk_prova = %s'
    cursor = conexao.cursor()
    cursor.execute(query, (pk_prova))

    provaBuscada = cursor.fetchone()[0]
    cursor.close()
    conexao.close()

    if provaBuscada is None:
        return None

    return provaBuscada[0]