from ..Cadastrar.criarConexao import criarConexao


def deletarProvaAtletismo(pk_prova):
    """Exclui resultados, inscrições e a prova na ordem exigida pelas FKs."""
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                "DELETE FROM recordes_atletismo WHERE fk_prova = %s",
                (pk_prova,),
            )
            cursor.execute(
                "DELETE FROM inscricoes_provas_atletismo WHERE fk_prova = %s",
                (pk_prova,),
            )
            cursor.execute(
                "DELETE FROM provas_atletismo WHERE pk_prova = %s",
                (pk_prova,),
            )
            if cursor.rowcount == 0:
                raise ValueError("Prova não encontrada.")
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()
