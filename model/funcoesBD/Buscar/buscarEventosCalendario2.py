from ..Cadastrar.criarConexao import criarConexao


def buscarEventosCalendario():
    banco = criarConexao()
    cursor = banco.cursor(dictionary=True)

    sql = """
        SELECT
            c.pk_evento,
            c.dia_evento,
            c.hora_inicio,
            c.hora_fim,

            p.fk_esporte,
            p.fk_genero,

            tc.pk_nome_turma AS equipe_casa,
            tv.pk_nome_turma AS equipe_visitante

        FROM calendario c

        INNER JOIN partidas p
            ON c.fk_partida = p.pk_partida

        INNER JOIN equipes ec
            ON p.fk_equipe_casa = ec.pk_equipe

        INNER JOIN equipes ev
            ON p.fk_equipe_visitante = ev.pk_equipe

        INNER JOIN turmas tc
            ON ec.fk_nome_turma = tc.pk_nome_turma

        INNER JOIN turmas tv
            ON ev.fk_nome_turma = tv.pk_nome_turma
    """

    cursor.execute(sql)

    eventos = cursor.fetchall()

    cursor.close()
    banco.close()

    return eventos