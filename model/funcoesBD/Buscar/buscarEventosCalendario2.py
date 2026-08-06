from model.conexao import conectarBanco


def buscarEventosCalendario():

    banco = conectarBanco()
    cursor = banco.cursor(dictionary=True)

    sql = """
        SELECT
            c.pk_evento,
            c.dia_evento,
            c.hora_inicio,
            c.hora_fim,

            p.fk_esporte,

            ec.nome_equipe AS equipe_casa,
            ev.nome_equipe AS equipe_visitante

        FROM calendario c

        INNER JOIN partidas p
            ON c.fk_partida = p.pk_partida

        INNER JOIN equipes ec
            ON p.fk_equipe_casa = ec.pk_equipe

        INNER JOIN equipes ev
            ON p.fk_equipe_visitante = ev.pk_equipe
    """

    cursor.execute(sql)

    eventos = cursor.fetchall()

    cursor.close()
    banco.close()

    return eventos