from .criarConexao import criarConexao, database

def cadastrarUsuario(pk_usuario, senha, nivel, fk_nome_turma=None):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            
            query = """
                INSERT INTO login (pk_usuario, senha, nivel, fk_nome_turma)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(query, (pk_usuario, senha, nivel, fk_nome_turma))
            usuario_cadastrado = cursor.lastrowid()[0]
        conexao.commit()
    finally:
        conexao.close()