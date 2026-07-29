from .criarConexao import criarConexao
from ...funcoesLOG.LOG import criarLOGInfo

def cadastrarEquipe(esporte, turma, genero, alunos, usuario_logado):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            # Pega limite do esporte
            cursor.execute("SELECT qtd_jogadores FROM esportes WHERE pk_esporte=%s", (esporte,))
            limite = cursor.fetchone()[0]

            if len(alunos) > limite:
                raise ValueError(f"O esporte só permite até {limite} jogadores.")

            query = """
                INSERT INTO equipes (fk_esporte, fk_nome_turma, fk_genero)
                VALUES (%s, %s, %s)
            """
            params = (esporte, turma, genero)
            criarLOGInfo(query, cursor, params, usuario_logado, params)
            id_equipe = cursor.lastrowid

            for matricula in alunos:
                cursor.execute("""
                    INSERT INTO membros_equipe (fk_equipe, fk_matricula)
                    VALUES (%s, %s)
                """, (id_equipe, matricula))

        conexao.commit()
    finally:
        conexao.close()