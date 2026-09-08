from ..Cadastrar.criarConexao import criarConexao, database


def buscarProvasProximas():

    conexao = criarConexao()

    try:

        with conexao.cursor(dictionary=True) as cursor:

            cursor.execute(f"""
                SELECT
                    p.pk_prova,
                    p.fk_modalidade,
                    p.fk_genero,
                    p.nome_prova,
                    p.tipo_resultado,
                    p.unidade_medida,
                    p.data_prova,

                    m.nome_modalidade,
                    c.pk_genero

                FROM {database}.provas_atletismo p

                INNER JOIN {database}.modalidades_atletismo m
                    ON p.fk_modalidade = m.pk_modalidade

                INNER JOIN {database}.classificacao c
                    ON p.fk_genero = c.pk_genero

                WHERE p.data_prova >= NOW()
                  AND p.data_prova <= DATE_ADD(NOW(), INTERVAL 2 HOUR)

                ORDER BY p.data_prova ASC
            """)

            return cursor.fetchall()

    finally:

        conexao.close()