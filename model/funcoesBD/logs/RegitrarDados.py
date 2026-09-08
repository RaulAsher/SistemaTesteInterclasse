from ..Cadastrar.criarConexao import criarConexao, database



def registrar_log(usuario, acao):
    conexao = criarConexao()
    cursor= conexao.cursor()
    cursor.execute("""
        INSERT INTO logs(usuario, acao)
        VALUES (%s, %s)
    """, (usuario, acao))

    conexao.commit()