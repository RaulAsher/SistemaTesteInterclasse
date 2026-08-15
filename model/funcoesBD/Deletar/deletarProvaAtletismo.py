from ..Cadastrar.criarConexao import criarConexao


def deletarProvaAtletismo(pk_prova):
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        # Primeiro remove os atletas inscritos nessa prova
        cursor.execute(
            """
            DELETE FROM inscricoes_provas_atletismo
            WHERE fk_prova = %s
            """,
            (pk_prova,)
        )

        # Depois remove a própria prova
        cursor.execute(
            """
            DELETE FROM provas_atletismo
            WHERE pk_prova = %s
            """,
            (pk_prova,)
        )

        # Verifica se alguma prova realmente foi excluída
        if cursor.rowcount == 0:
            raise Exception("Prova não encontrada.")

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()