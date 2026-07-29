from .criarConexao import criarConexao, database

def cadastrarAluno(matricula, nome, turma, genero):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            query = """
                INSERT INTO alunos (pk_matricula, nome_aluno, fk_nome_turma, fk_classificacao)
                VALUES (%s, %s, %s, %s)
            """
            params = (matricula, nome, turma, genero)


            cursor.execute(query, params)
        conexao.commit()
    finally:
        conexao.close()
