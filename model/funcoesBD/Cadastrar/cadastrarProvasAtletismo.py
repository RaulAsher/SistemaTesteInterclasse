from ..Cadastrar.criarConexao import criarConexao, database

def cadastrarProvaAtletismo(
    fk_modalidade,
    fk_genero,
    nome_prova,
    tipo_resultado,
    unidade_medida,
    data_hora=None
):
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:

        # =========================
        # 1. CADASTRAR A PROVA
        # =========================

        sql_prova = """
            INSERT INTO provas_atletismo (
                fk_modalidade,
                fk_genero,
                nome_prova,
                tipo_resultado,
                unidade_medida
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        valores_prova = (
            fk_modalidade,
            fk_genero,
            nome_prova,
            tipo_resultado,
            unidade_medida
        )

        cursor.execute(sql_prova, valores_prova)

        fk_prova = cursor.lastrowid


        # =========================
        # 2. CRIAR A PARTIDA
        # =========================

        sql_partida = """
            INSERT INTO partidas (
                fk_genero,
                definida,
                fk_prova
            )
            VALUES (%s, 'nao', %s)
        """

        cursor.execute(
            sql_partida,
            (fk_genero, fk_prova)
        )

        fk_partida = cursor.lastrowid


        # =========================
        # 3. CRIAR EVENTO NO CALENDÁRIO
        # =========================

        if data_hora:

            data = data_hora.replace("T", " ")

            from datetime import datetime

            data_hora_obj = datetime.strptime(
                data,
                "%Y-%m-%d %H:%M"
            )

            sql_calendario = """
                INSERT INTO calendario (
                    dia_evento,
                    fk_partida,
                    hora_inicio
                )
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                sql_calendario,
                (
                    data_hora_obj.date(),
                    fk_partida,
                    data_hora_obj.time()
                )
            )


        conexao.commit()

        return fk_prova

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()