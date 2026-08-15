from ..Cadastrar.criarConexao import criarConexao, database

def buscarProvas():

    conexao = criarConexao()
    cursor = conexao.cursor()
    query = """
            SELECT 
                p.pk_prova,           -- [0]
                p.fk_modalidade,      -- [1]
                p.fk_genero,          -- [2]
                p.nome_prova,         -- [3]
                p.tipo_resultado,     -- [4]
                p.unidade_medida,     -- [5]
                p.ativo,              -- [6]
                COUNT(i.fk_matricula) AS total_participantes, -- [7]
                COALESCE(p.status, 'nao_iniciada') AS status   -- [8] Coluna de status
            FROM provas_atletismo p
            LEFT JOIN inscricoes_provas_atletismo i ON p.pk_prova = i.fk_prova
            WHERE p.ativo = 1
            GROUP BY p.pk_prova;
        """
    cursor.execute(query)
    provas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return provas