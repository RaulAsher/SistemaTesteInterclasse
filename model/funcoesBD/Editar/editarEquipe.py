from datetime import datetime, timedelta
from ..Cadastrar.criarConexao import criarConexao, database

def editarEquipe(pk_equipe, esporte, turma, genero, alunos):
    conexao = criarConexao()
    try:
        with conexao.cursor() as cursor:
            # Verificar limite do esporte
            cursor.execute("SELECT qtd_jogadores FROM esportes WHERE pk_esporte=%s", (esporte,))
            limite = cursor.fetchone()[0]

            if len(alunos) > limite:
                raise ValueError(f"O esporte selecionado permite no máximo {limite} jogadores.")

            # Atualizar dados principais
            cursor.execute("""
                UPDATE equipes
                SET fk_esporte=%s, fk_nome_turma=%s, fk_genero=%s
                WHERE pk_equipe=%s
            """, (esporte, turma, genero, pk_equipe))

            # Apagar jogadores antigos
            cursor.execute("DELETE FROM membros_equipe WHERE fk_equipe=%s", (pk_equipe,))

            # Inserir os novos
            for matricula in alunos:
                cursor.execute("""
                    INSERT INTO membros_equipe (fk_equipe, fk_matricula)
                    VALUES (%s, %s)
                """, (pk_equipe, matricula))

        conexao.commit()
    finally:
        conexao.close()


def edicaoEquipesPermitida():
    conexao = criarConexao()

    if not conexao:
        return False

    try:
        with conexao.cursor() as cursor:

            # Busca a quantidade de dias permitida
            cursor.execute("""
                SELECT valor
                FROM configuracoes
                WHERE chave = 'prazo_edicao_equipes'
            """)

            resultado_prazo = cursor.fetchone()

            if resultado_prazo is None:
                return False

            prazo_dias = int(resultado_prazo[0])

            # Busca a data em que o prazo começou
            cursor.execute("""
                SELECT valor
                FROM configuracoes
                WHERE chave = 'inicio_prazo_edicao_equipes'
            """)

            resultado_inicio = cursor.fetchone()

            if resultado_inicio is None:
                return False

            inicio = resultado_inicio[0]

            # Caso o banco retorne string
            if isinstance(inicio, str):
                inicio = datetime.strptime(
                    inicio,
                    "%Y-%m-%d %H:%M:%S"
                )

            # Calcula o fim do prazo
            fim_prazo = inicio + timedelta(days=prazo_dias)

            # Verifica se ainda está dentro do período
            return datetime.now() <= fim_prazo

    finally:
        conexao.close()