from .criarConexao import criarConexao, database

def cadastrarEquipe(esporte, turma, genero, alunos):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            # Pega limite do esporte
            cursor.execute("SELECT qtd_jogadores FROM esportes WHERE pk_esporte=%s", (esporte,))
            limite = cursor.fetchone()[0]

            if len(alunos) > limite:
                raise ValueError(f"O esporte só permite até {limite} jogadores.")

            cursor.execute("""
                INSERT INTO equipes (fk_esporte, fk_nome_turma, fk_genero)
                VALUES (%s, %s, %s)
            """, (esporte, turma, genero))
            id_equipe = cursor.lastrowid

            for matricula in alunos:
                cursor.execute("""
                    INSERT INTO membros_equipe (fk_equipe, fk_matricula)
                    VALUES (%s, %s)
                """, (id_equipe, matricula))

        conexao.commit()
    finally:
        conexao.close()
