from ..Cadastrar.criarConexao import criarConexao, database

def buscarModalidades():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.esportes')

    modalidadesBuscadas = cursor.fetchall()

    return modalidadesBuscadas

def buscarModalidadesAtletismo():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            pk_modalidade,
            nome_modalidade,
            genero,
            ativo
        FROM modalidades_atletismo
        ORDER BY nome_modalidade
    """)

    modalidades = cursor.fetchall()

    cursor.close()
    conexao.close()

    return modalidades