from ..Cadastrar.criarConexao import criarConexao, database

def editarAluno(nova_matricula, nome, turma, genero, antiga_matricula):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            query = "UPDATE alunos SET pk_matricula=%s, nome_aluno=%s, fk_nome_turma=%s, fk_classificacao=%s WHERE pk_matricula=%s"
            cursor.execute(query, (nova_matricula, nome, turma, genero, antiga_matricula))
        conexao.commit()
    finally:
        conexao.close()
