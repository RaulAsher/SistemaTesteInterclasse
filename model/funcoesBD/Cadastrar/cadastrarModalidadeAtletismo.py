from ..Cadastrar.criarConexao import criarConexao, database


def cadastrarModalidadeAtletismo(nome_modalidade, descricao=None, ativo=1):

    conexao = criarConexao()

    try:

        with conexao.cursor() as cursor:

            cursor.execute(
                f"""
                INSERT INTO {database}.modalidades_atletismo
                    (nome_modalidade, descricao, ativo)
                VALUES
                    (%s, %s, %s)
                """,
                (
                    nome_modalidade,
                    descricao,
                    ativo
                )
            )

            conexao.commit()

            pk_modalidade = cursor.lastrowid

            return pk_modalidade

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()