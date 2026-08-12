from ..Cadastrar.criarConexao import criarConexao, database

def alterarConfiguracao(chave, valor):
    conexao = criarConexao()
    cursor = conexao.cursor()
    
    cursor.execute("""
        UPDATE configuracoes
        SET valor = %s
        WHERE chave = %s
    """, (valor, chave))

    conexao.commit()

def buscarConfiguracao(chave):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT valor
        FROM configuracoes
        WHERE chave = %s
    """, (chave,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return resultado["valor"]

    return None