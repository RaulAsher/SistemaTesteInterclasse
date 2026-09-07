from ..Cadastrar.criarConexao import criarConexao


def buscarAlunosPorTurma(turma):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    a.pk_matricula,
                    a.nome_aluno,
                    a.fk_nome_turma,
                    a.fk_classificacao,
                    t.icone_url
                FROM alunos AS a
                LEFT JOIN turmas AS t
                    ON a.fk_nome_turma = t.pk_nome_turma
                WHERE a.fk_nome_turma = %s
                ORDER BY a.nome_aluno ASC
            """, (turma,))
            return cursor.fetchall()
    finally:
        conexao.close()
