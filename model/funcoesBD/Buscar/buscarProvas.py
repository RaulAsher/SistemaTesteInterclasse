from ..Cadastrar.criarConexao import criarConexao


def buscarProvas():
    """Retorna todas as provas, inclusive as finalizadas, com total de inscritos."""
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.pk_prova,
                    p.fk_modalidade,
                    p.fk_genero,
                    p.nome_prova,
                    p.tipo_resultado,
                    p.unidade_medida,
                    COALESCE(p.status, 'nao_iniciada') AS status,
                    COUNT(DISTINCT i.fk_matricula) AS total_participantes
                FROM provas_atletismo p
                LEFT JOIN inscricoes_provas_atletismo i
                    ON i.fk_prova = p.pk_prova
                GROUP BY
                    p.pk_prova,
                    p.fk_modalidade,
                    p.fk_genero,
                    p.nome_prova,
                    p.tipo_resultado,
                    p.unidade_medida,
                    p.status
                ORDER BY p.data_prova IS NULL, p.data_prova, p.nome_prova
                """
            )
            return cursor.fetchall()
    finally:
        conexao.close()
