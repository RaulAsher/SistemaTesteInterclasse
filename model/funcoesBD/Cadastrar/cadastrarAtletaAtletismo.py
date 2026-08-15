from ..Cadastrar.criarConexao import criarConexao, database

def cadastrarAtletaAtletismo(fk_prova, fk_matricula):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()
        
        cursor.execute(
            "INSERT INTO inscricoes_provas_atletismo (fk_prova, fk_matricula) VALUES (%s, %s)",
            (fk_prova, fk_matricula)
        )
        
        conexao.commit()
    except Exception as e:
        print("Erro ao cadastrar atleta no banco:", e)
        if conexao:
            conexao.rollback()
        raise e
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conexao' in locals() and conexao:
            conexao.close() # CRUCIAL: Fechar a conexão