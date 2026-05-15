from ..Cadastrar.criarConexao import criarConexao, database

# Buscar alunos de uma turma
def alunosPorTurmaListaEquipes(nome_turma, classificacao, modalidade):
    conexao = criarConexao()
    try:
        with conexao.cursor(dictionary=True) as cursor:
            if classificacao == "Misto":
                query = """
                    SELECT a.pk_matricula AS matricula,
                    	   a.nome_aluno AS nome

                    FROM alunos a

                    WHERE
                    (SELECT me.fk_matricula 
                       
                       FROM membros_equipe me

                        left join equipes e
                        on e.pk_equipe = me.fk_equipe

                        WHERE me.fk_matricula = a.pk_matricula 
                        and e.fk_esporte = %s) is null
                    AND a.fk_nome_turma = %s order by a.nome_aluno
                """
                cursor.execute(query, (modalidade,nome_turma))
            else:
                query = """
                    SELECT a.pk_matricula AS matricula,
                           a.nome_aluno AS nome
                    FROM alunos a

                    WHERE 
                      (SELECT me.fk_matricula 
                       
                       FROM membros_equipe me

                        left join equipes e
                        on e.pk_equipe = me.fk_equipe

                        WHERE me.fk_matricula = a.pk_matricula 
                        and e.fk_esporte = %s) is null  
                      AND a.fk_nome_turma = %s
                      AND a.fk_classificacao = %s
                      
                      order by nome_aluno
                """
                cursor.execute(query, (modalidade,nome_turma, classificacao))

            return cursor.fetchall()
    finally:
        conexao.close()
