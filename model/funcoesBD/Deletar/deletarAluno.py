from ..Cadastrar.criarConexao import criarConexao, database
from ...funcoesLOG.LOG import criarLOGInfo

def deletarAluno(matricula, usuario_logado):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT nome_aluno,fk_nome_turma FROM alunos WHERE pk_matricula=%s", (matricula,))
            aluno_deletado = cursor.fetchone()

            if aluno_deletado is not None:
                nome_aluno, fk_nome_turma = aluno_deletado
                
                query = "DELETE FROM alunos WHERE pk_matricula=%s"
                params = (matricula, nome_aluno, fk_nome_turma)
                criarLOGInfo(query, cursor, params, usuario_logado)
            conexao.commit()
    finally:
        conexao.close()
