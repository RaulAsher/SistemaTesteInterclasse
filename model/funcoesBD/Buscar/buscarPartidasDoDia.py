from ..Cadastrar.criarConexao import criarConexao


def buscarPartidasDoDia():

    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    try:

        query = """
            SELECT
                p.pk_partida,
                p.fk_esporte,
                p.fk_genero,
                p.fk_equipe_casa,
                p.fk_equipe_visitante,
                p.pontos_turma_casa,
                p.pontos_turma_visitante,
                p.definida,
                p.par_re1,
                p.par_re2,
                p.etapa,
                p.pk_partida_mae,
                p.pk_equipe_vencedora,
                p.data_hora,

                ec.fk_nome_turma AS turma_casa,
                ev.fk_nome_turma AS turma_visitante

            FROM partidas p

            LEFT JOIN equipes ec
                ON p.fk_equipe_casa = ec.pk_equipe

            LEFT JOIN equipes ev
                ON p.fk_equipe_visitante = ev.pk_equipe

            WHERE DATE(p.data_hora) = CURDATE()

            ORDER BY p.data_hora ASC
        """

        cursor.execute(query)

        partidas = cursor.fetchall()

        print("======================================")
        print("PARTIDAS DE HOJE:")
        print(partidas)
        print("======================================")

        return partidas

    except Exception as erro:

        print("ERRO AO BUSCAR PARTIDAS DO DIA:", erro)

        return []

    finally:

        cursor.close()
        conexao.close()