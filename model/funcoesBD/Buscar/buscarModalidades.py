from ..Cadastrar.criarConexao import criarConexao, database


def buscarModalidades():

    conexao = criarConexao()

    try:

        with conexao.cursor(dictionary=True) as cursor:

            # ==========================================
            # 1. BUSCAR ESPORTES
            # ==========================================

            cursor.execute(f"""
                SELECT *
                FROM {database}.esportes
                ORDER BY grupo, pk_esporte
            """)

            esportes = cursor.fetchall()


            # ==========================================
            # 2. SEPARAR ESPORTES
            # ==========================================

            esportesAtletismo = []
            esportesOutros = []

            for esporte in esportes:

                pk_esporte = str(
                    esporte.get("pk_esporte") or ""
                ).strip().lower()

                grupo = str(
                    esporte.get("grupo") or ""
                ).strip().lower()

                if (
                    pk_esporte == "atletismo"
                    or grupo == "atletismo"
                ):
                    esportesAtletismo.append(esporte)

                else:
                    esportesOutros.append(esporte)


            # ==========================================
            # 3. BUSCAR MODALIDADES DO ATLETISMO
            # ==========================================

            cursor.execute(f"""
                SELECT
                    pk_modalidade,
                    nome_modalidade,
                    descricao,
                    ativo
                FROM {database}.modalidades_atletismo
                ORDER BY nome_modalidade
            """)

            modalidadesAtletismo = cursor.fetchall()


            # ==========================================
            # 4. RETORNO
            # ==========================================

            return {
                "esportes_atletismo": esportesAtletismo,
                "modalidades_atletismo": modalidadesAtletismo,
                "esportes_outros": esportesOutros
            }

    finally:

        conexao.close()

        