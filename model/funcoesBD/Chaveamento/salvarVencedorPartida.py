from ..Cadastrar.criarConexao import criarConexao
import mysql.connector


def atualizarPartidaProximaRodada(cod_partida_mae, partida_id, vencedor_id):

    # Caso seja a final, não existe próxima partida
    if cod_partida_mae in (None, "", "NULL", "null"):
        return True

    conexao = criarConexao()

    if not conexao:
        return False

    try:

        with conexao.cursor() as cursor:

            query1 = """
                SELECT MAX(pk_partida) AS cod_partida_visitante
                FROM etemfl83_inter_classe.partidas
                WHERE pk_partida_mae = %s;
            """

            cursor.execute(query1, (cod_partida_mae,))
            cod_partida_visitante = cursor.fetchone()

            # Segurança
            if (
                cod_partida_visitante is None
                or
                cod_partida_visitante[0] is None
            ):
                return True

    except mysql.connector.Error as err:

        print(f"Erro ao buscar próxima partida: {err}")

        return False

    if cod_partida_visitante[0] > int(partida_id):

        query = """
            UPDATE partidas
            SET fk_equipe_casa = %s
            WHERE pk_partida = %s
            AND definida = 'nao';
        """

    else:

        query = """
            UPDATE partidas
            SET fk_equipe_visitante = %s
            WHERE pk_partida = %s
            AND definida = 'nao';
        """

    try:

        with conexao.cursor() as cursor:

            cursor.execute(query, (vencedor_id, cod_partida_mae))

            conexao.commit()

            return True

    except mysql.connector.Error as err:

        print(f"Erro ao atualizar próxima partida: {err}")

        return False

    finally:

        conexao.close()


def salvarVencedorPartida(
    partida_id,
    vencedor_id,
    pontos_equipe_casa,
    pontos_equipe_visitante,
    cod_partida_mae
):

    conexao = criarConexao()

    if not conexao:
        return False

    try:

        # Salva o resultado da partida

        with conexao.cursor() as cursor:

            query = """
                UPDATE partidas

                SET
                    pk_equipe_vencedora = %s,
                    definida = 'sim',
                    pontos_turma_casa = %s,
                    pontos_turma_visitante = %s

                WHERE
                    pk_partida = %s
                    AND definida = 'nao';
            """

            cursor.execute(
                query,
                (
                    vencedor_id,
                    pontos_equipe_casa,
                    pontos_equipe_visitante,
                    partida_id
                )
            )

            conexao.commit()

    except mysql.connector.Error as err:

        print(f"Erro ao salvar vencedor: {err}")

        return False

    finally:

        conexao.close()

    # Atualiza a próxima rodada (caso exista)

    atualizarPartidaProximaRodada(
        cod_partida_mae,
        partida_id,
        vencedor_id
    )

    return True