from ..Cadastrar.criarConexao import criarConexao

def getAlunoEquipe(idEquipe):
    """
    Buscar aluno da equipe individual
    """
    conexao = criarConexao()
    if not conexao: return []

    try:
        with conexao.cursor(dictionary=True) as cursor: 
            query = """select CONCAT(SUBSTRING_INDEX(a.nome_aluno, ' ', 1),' ',SUBSTRING_INDEX(a.nome_aluno, ' ', -1)) as nome_aluno

                        from etemfl83_inter_classe.membros_equipe me

                        left join etemfl83_inter_classe.alunos a
                        on a.pk_matricula = me.fk_matricula

                        where me.fk_equipe = %s;"""
            cursor.execute(query, (idEquipe,)) 
            resultado = cursor.fetchone()
            if not resultado:
                return ''
            else:
                return resultado['nome_aluno']
    finally:
        conexao.close()