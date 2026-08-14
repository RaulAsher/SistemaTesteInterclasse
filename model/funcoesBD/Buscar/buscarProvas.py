from ..Cadastrar.criarConexao import criarConexao, database

def buscarProvas():

    conexao = criarConexao()

    query = 'SELECT * FROM provas_atletismo'
    cursor = conexao.cursor()

    cursor.execute(query)

    provasBuscadas = cursor.fetchall()

    if provasBuscadas == None:
        return None

    return provasBuscadas