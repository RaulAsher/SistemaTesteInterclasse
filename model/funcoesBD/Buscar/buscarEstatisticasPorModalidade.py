from ..Cadastrar.criarConexao import criarConexao
from flask import flash


def buscarEstatisticasPorModalidade(modalidade):
    conexao = None
    cursor = None

    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        query = """
            SELECT fk_nome_estatistica, estatistica_principal
            FROM estatisticas_esporte
            WHERE fk_esporte = %s
        """

        cursor.execute(query, (modalidade,))
        estatisticasBuscadas = cursor.fetchall()

        return estatisticasBuscadas

    except Exception as erro:
        print(f"Erro ao buscar estatísticas da modalidade: {erro}")

        flash(
            "Não foi possível carregar as estatísticas da modalidade.",
            "error"
        )

        return []

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()