from ..Cadastrar.criarConexao import criarConexao
import mysql.connector

def atualizarPartidaProximaRodada(cod_partida_mae, partida_id , vencedor_id):
    conexao = criarConexao()
    if not conexao: return False
    cod_partida_visitante = None
    try:
        with conexao.cursor() as cursor:
            query1 = """
                    SELECT Max(pk_partida) as cod_partida_visitante 
                    FROM etemfl83_inter_classe.partidas p 
                    where p.pk_partida_mae = %s;
                    """
            cursor.execute(query1, (cod_partida_mae,))
            cod_partida_visitante = cursor.fetchone()
            
    except mysql.connector.Error as err:
        print(f"Erro ao salvar vencedor: {err}")

    query = None
    if(cod_partida_visitante[0] > int(partida_id)):
        query = """
            UPDATE partidas
            SET fk_equipe_casa = %s
            WHERE pk_partida = %s AND definida = 'nao';
            """
    else:
        query = """
            UPDATE partidas
            SET fk_equipe_visitante = %s
            WHERE pk_partida = %s AND definida = 'nao';
            """

    try:
        with conexao.cursor() as cursor:
            cursor.execute(query, (vencedor_id, cod_partida_mae))
            conexao.commit()
            return cursor.rowcount > 0
    except mysql.connector.Error as err:
        print(f"Erro ao salvar vencedor: {err}")
        return False
    finally:
        conexao.close()

def salvarVencedorPartida(partida_id, vencedor_id, pontos_equipe_casa, pontos_equipe_Visitante, cod_partida_mae):
    """
    Registra o vencedor de uma partida e marca como 'sim' (definida).
    """

    atualizarPartidaProximaRodada(cod_partida_mae,partida_id,vencedor_id)

    conexao = criarConexao()
    if not conexao: return False

    try:
        with conexao.cursor() as cursor:
            query = """
            UPDATE partidas
            SET pk_equipe_vencedora = %s, definida = 'sim',
            pontos_turma_casa = %s, 
            pontos_turma_visitante = %s
            WHERE pk_partida = %s AND definida = 'nao';
            """
            cursor.execute(query, (vencedor_id, pontos_equipe_casa, pontos_equipe_Visitante ,partida_id))
            conexao.commit()
            return cursor.rowcount > 0
    except mysql.connector.Error as err:
        print(f"Erro ao salvar vencedor: {err}")
        return False
    finally:
        conexao.close()