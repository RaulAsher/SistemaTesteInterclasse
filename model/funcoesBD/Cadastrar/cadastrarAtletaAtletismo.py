from ..Cadastrar.criarConexao import criarConexao


def cadastrarAtletaAtletismo(fk_prova, fk_matricula):
    """Inscreve um atleta uma única vez, respeitando o gênero da prova."""
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1
                FROM provas_atletismo p
                INNER JOIN alunos a ON a.pk_matricula = %s
                WHERE p.pk_prova = %s
                  AND (p.fk_genero = 'Misto' OR p.fk_genero = a.fk_classificacao)
                """,
                (fk_matricula, fk_prova),
            )
            if cursor.fetchone() is None:
                raise ValueError("Atleta ou prova inválidos, ou gênero incompatível.")

            cursor.execute(
                """
                SELECT 1
                FROM inscricoes_provas_atletismo
                WHERE fk_prova = %s AND fk_matricula = %s
                """,
                (fk_prova, fk_matricula),
            )
            if cursor.fetchone() is not None:
                raise ValueError("Este atleta já está inscrito nesta prova.")

            cursor.execute(
                """
                INSERT INTO inscricoes_provas_atletismo (fk_prova, fk_matricula)
                VALUES (%s, %s)
                """,
                (fk_prova, fk_matricula),
            )
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()
