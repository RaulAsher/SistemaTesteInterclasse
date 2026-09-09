from ..Cadastrar.criarConexao import criarConexao


def buscarAtletasAtletismo():
    """Lista inscrições e calcula a classificação por prova.

    Para provas de tempo, o menor resultado vence. Para distância, altura e
    pontos, vence o maior resultado. Caso exista mais de um registro do mesmo
    atleta na mesma prova, somente o melhor é considerado no ranking.
    """
    conexao = criarConexao()

    try:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(
                """
                WITH melhores_resultados AS (
                    SELECT
                        r.fk_prova,
                        r.fk_matricula,
                        CASE
                            WHEN p.tipo_resultado = 'tempo' THEN MIN(r.resultado)
                            ELSE MAX(r.resultado)
                        END AS resultado
                    FROM recordes_atletismo r
                    INNER JOIN provas_atletismo p
                        ON p.pk_prova = r.fk_prova
                    GROUP BY r.fk_prova, r.fk_matricula, p.tipo_resultado
                ), inscritos AS (
                    SELECT
                        p.pk_prova,
                        p.nome_prova,
                        p.tipo_resultado,
                        p.unidade_medida,
                        p.fk_genero AS genero,
                        a.pk_matricula AS matricula,
                        a.nome_aluno,
                        a.fk_nome_turma AS turma,
                        mr.resultado,
                        RANK() OVER (
                            PARTITION BY p.pk_prova
                            ORDER BY
                                CASE WHEN p.tipo_resultado = 'tempo'
                                    THEN mr.resultado END ASC,
                                CASE WHEN p.tipo_resultado <> 'tempo'
                                    THEN mr.resultado END DESC
                        ) AS posicao_calculada
                    FROM inscricoes_provas_atletismo i
                    INNER JOIN provas_atletismo p
                        ON p.pk_prova = i.fk_prova
                    INNER JOIN alunos a
                        ON a.pk_matricula = i.fk_matricula
                    LEFT JOIN melhores_resultados mr
                        ON mr.fk_prova = i.fk_prova
                       AND mr.fk_matricula = i.fk_matricula
                )
                SELECT
                    pk_prova,
                    nome_prova,
                    tipo_resultado,
                    unidade_medida,
                    genero,
                    matricula,
                    nome_aluno,
                    turma,
                    resultado,
                    CASE
                        WHEN resultado IS NULL THEN NULL
                        ELSE posicao_calculada
                    END AS posicao
                FROM inscritos
                ORDER BY
                    nome_prova,
                    resultado IS NULL,
                    posicao,
                    nome_aluno
                """
            )
            return cursor.fetchall()
    finally:
        conexao.close()
