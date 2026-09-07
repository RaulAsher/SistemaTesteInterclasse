from ..Cadastrar.criarConexao import criarConexao


def buscarAlunos():
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT pk_matricula, nome_aluno, fk_nome_turma, fk_classificacao
                FROM alunos
                ORDER BY nome_aluno ASC
            """)
            return cursor.fetchall()
    finally:
        conexao.close()
