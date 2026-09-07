from ..Cadastrar.criarConexao import criarConexao


def buscarEquipesPorModCla(esporte, classificacao):
    conexao = criarConexao()
    try:
        with conexao.cursor(dictionary=True) as cursor:
            query = """
                SELECT
                    e.pk_equipe,
                    s.pk_esporte AS esporte,
                    t.pk_nome_turma AS turma,
                    c.pk_genero AS classificacao,
                    e.nome_equipe,
                    s.grupo,
                    s.qtd_jogadores
                FROM equipes AS e
                JOIN esportes AS s
                    ON e.fk_esporte = s.pk_esporte
                JOIN turmas AS t
                    ON e.fk_nome_turma = t.pk_nome_turma
                JOIN classificacao AS c
                    ON e.fk_genero = c.pk_genero
                WHERE s.pk_esporte = %s
                  AND c.pk_genero = %s
                ORDER BY t.pk_nome_turma ASC, e.nome_equipe ASC
            """
            cursor.execute(query, (esporte, classificacao))
            return cursor.fetchall()
    finally:
        conexao.close()
