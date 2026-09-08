from ..Cadastrar.criarConexao import criarConexao

def buscarTipoModalidade(modalidade):
    conexao = criarConexao()
    if not conexao: return []
    
    try:
        with conexao.cursor(dictionary=True) as cursor: 
            query = '''SELECT grupo FROM esportes where pk_esporte=%s;'''
            cursor.execute(query, (modalidade,))
            resultado = cursor.fetchone()
            if not resultado:
                return None
            else:
                return resultado['grupo']

    finally:
        conexao.close()

    