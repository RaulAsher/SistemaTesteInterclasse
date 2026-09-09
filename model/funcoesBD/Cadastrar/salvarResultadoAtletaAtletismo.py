from decimal import Decimal, InvalidOperation

from ..Cadastrar.criarConexao import criarConexao


def salvarResultadoAtletaAtletismo(fk_prova, fk_matricula, resultado):
    """Registra ou atualiza o resultado de um atleta já inscrito na prova."""
    try:
        resultado = Decimal(str(resultado))
    except (InvalidOperation, TypeError, ValueError) as erro:
        raise ValueError("Informe um resultado numérico válido.") from erro

    if resultado < 0:
        raise ValueError("O resultado não pode ser negativo.")

    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1
                FROM inscricoes_provas_atletismo
                WHERE fk_prova = %s AND fk_matricula = %s
                """,
                (fk_prova, fk_matricula),
            )
            if cursor.fetchone() is None:
                raise ValueError("O atleta não está inscrito nesta prova.")

            cursor.execute(
                """
                SELECT pk_recorde
                FROM recordes_atletismo
                WHERE fk_prova = %s AND fk_matricula = %s
                ORDER BY pk_recorde DESC
                LIMIT 1
                """,
                (fk_prova, fk_matricula),
            )
            registro = cursor.fetchone()

            if registro:
                cursor.execute(
                    """
                    UPDATE recordes_atletismo
                    SET resultado = %s, data_recorde = CURDATE(), ano = YEAR(CURDATE())
                    WHERE pk_recorde = %s
                    """,
                    (resultado, registro[0]),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO recordes_atletismo
                        (fk_prova, fk_matricula, resultado, data_recorde, ano)
                    VALUES (%s, %s, %s, CURDATE(), YEAR(CURDATE()))
                    """,
                    (fk_prova, fk_matricula, resultado),
                )

        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()
