from .criarConexao import criarConexao, database
from ...funcoesLOG.LOG import criarLOGInfo

def cadastrarAluno(matricula, nome, turma, genero, usuario_logado):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            query = """
                INSERT INTO alunos (pk_matricula, nome_aluno, fk_nome_turma, fk_classificacao)
                VALUES (%s, %s, %s, %s)
            """
            params = (matricula, nome, turma, genero)


            criarLOGInfo(query, cursor, params, usuario_logado)
        conexao.commit()
    finally:
        conexao.close()
