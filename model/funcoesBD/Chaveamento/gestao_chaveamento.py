import math
import random
import mysql.connector

# IMPORTAÇÕES RELATIVAS CORRIGIDAS:

# 1. Importa a função de busca de equipes (assumindo que está em um arquivo irmão)
#    Se o arquivo for 'buscarEquipesPorModCla.py' na mesma pasta.
from .buscarEquipesPorModCla import buscarEquipesPorModCla

# 2. Importa a conexão (assumindo que está em funcoesBD/Cadastrar/criarConexao.py)
#    Sobe um nível (..) para 'funcoesBD', desce para 'Cadastrar' e pega 'criarConexao'
from ..Cadastrar.criarConexao import criarConexao, database 


def gerar_chaveamento_sem_bye_contra_bye(equipes_ids):
    """
    Gera um chaveamento de mata-mata com semeadura, garantindo que BYEs não se enfrentem.
    
    “BYE” (ou “BYEs” no plural) significa basicamente:

    uma vaga automática para a próxima fase, sem precisar jogar.

    Args:
        equipes_ids (list): Uma lista de PKs (int) das equipes, JÁ ORDENADAS ou EMBARALHADAS
                            de acordo com a lógica de turmas/semeadura.
        
    Returns:
        list: Uma lista de listas, representando o chaveamento rodada por rodada.
    """
    n_equipes = len(equipes_ids)
    
    if n_equipes < 2:
        return []
    
    print('++++Gerando chaveamento++++')

    # Passo 1: Determinar o tamanho da chave e a quantidade de BYEs
    equipes_necessarias = 2 ** math.ceil(math.log2(n_equipes))
    n_byes = equipes_necessarias - n_equipes 
    
    print(f'Número de Byes: {n_byes}')

    for i in range(n_byes):
        equipes_ids.append(None)

    chaveamento_completo = []
    
    # Passo 2: Criar a primeira rodada com semeadura inversa (para equipes sem BYE)
    partidas_primeira_rodada = []
    
    partidas = int(equipes_necessarias/2)
    for i in range(partidas):
        equipe_1 = equipes_ids[i]
        # Lógica de semeadura inversa: primeiro vs último, segundo vs penúltimo, etc.
        equipe_2 = equipes_ids[len(equipes_ids) - 1 - i]
        partidas_primeira_rodada.append([equipe_1, equipe_2])
    
    chaveamento_completo.append(partidas_primeira_rodada)
    print(f'Cahveamento completo: {chaveamento_completo}')
    
    # # Passo 3: Simular as próximas rodadas
    # # Combina BYEs (que avançam automaticamente) com placeholders para os vencedores da 1ª rodada
    rodada_atual = partidas_primeira_rodada
    # print(f'Rodada Atual: {rodada_atual}')
    
    # Simula rodadas futuras (apenas para estruturar o chaveamento)
    while len(rodada_atual) > 1:
        partidas_rodada = []
        
        # Embaralha os participantes da rodada futura
        random.shuffle(rodada_atual)
        
        print(f'Rodada Atual2: {rodada_atual}')
        # Pareamento
        for i in range(0, len(rodada_atual), 2):
            partidas_rodada.append([rodada_atual[i], rodada_atual[i+1]])
        
        chaveamento_completo.append(partidas_rodada)
        print(f'Chaveamento completo: {chaveamento_completo}')
        print(f'Partidas roda: {partidas_rodada}')
        print(f'Valor de I: {i}')
        
        # Prepara a lista de "vencedores" para a próxima rodada
        rodada_atual = [None for i in range(len(partidas_rodada))]
        print(f'Rodada Atual3: {rodada_atual}')

    return chaveamento_completo


def getEquipe(partida):
    if partida != None:
        print(f"getEquipe - {partida}")
        print(f"getEquipe -  2º if: {isinstance(partida, list)}")
        if isinstance(partida, list):
            print(f"getEquipe -  3º if: {partida[0] != None and partida[1] != None}")
            if partida[0] != None and partida[1] != None:
                return None
            else:
                return partida[0]
        elif partida != None:
            return partida
    return None

def getEquipeVencedora(equipe_casa, equipe_visitante, etapa):
    if etapa > 1:
        return None
    elif equipe_casa is not None and equipe_visitante is not None:
        return None
    elif equipe_casa is None:
        return equipe_visitante
    else:
        return equipe_casa

def getPartidaDefinida(equipe_casa, equipe_visitante, etapa):
    if etapa > 1:
        return 'nao'
    elif(equipe_casa is not None and equipe_visitante is not None):
        return 'nao'
    else:
        return 'sim'
    
def salvar_partidas(chaveamento, esporte, classificacao):
    """Salva apenas as partidas da primeira rodada no banco de dados."""
    print("++++++++ Salvar Partidas +++++++++++")
    conexao = criarConexao()
    if not conexao:
        print("Erro: Não foi possível conectar ao banco de dados para salvar as partidas.")
        return 0
    
    cursor = conexao.cursor()
    partidas_inseridas = 0
    
    # Query para inserção na tabela 'partidas'
    query = """
        INSERT INTO partidas 
            (fk_esporte, fk_descricao, fk_equipe_casa, fk_equipe_visitante, etapa, definida, pk_partida_mae, pk_equipe_vencedora)
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    # A tupla de dados_partida já está correta com 5 elementos.

    # O chaveamento é uma lista de rodadas. Só salvamos a primeira (índice 0)
    # print(f'Chaveamento: {chaveamento}')


    etapa_atual = len(chaveamento)
    lista_id_rodas_mae_anteriores =  []
    for rodadas in reversed(chaveamento):
        print(f'rodada: {rodadas}')
        ids_rodadas_mae = []
        print(f'Etapa atual: {etapa_atual}')
        print(f'Lista Id Mãe Anterior: {lista_id_rodas_mae_anteriores}')
        contador_rodadas = 0
        for partida in rodadas:
            print(f'Lista Id Proxima Mãe: {ids_rodadas_mae}')

            equipe_casa =  getEquipe(partida[0])
            equipe_visitante = getEquipe(partida[1])
            
            # Na primeira rodada, todas as entradas que são PKs (int) são partidas reais.
            dados_partida = (
                esporte, 
                classificacao, 
                equipe_casa, 
                equipe_visitante, 
                etapa_atual,
                getPartidaDefinida(equipe_casa, equipe_visitante, etapa_atual),
                None if etapa_atual == len(chaveamento) else lista_id_rodas_mae_anteriores[0],
                getEquipeVencedora(equipe_casa, equipe_visitante, etapa_atual)
            )
            try:
                print(f"Dados inseridos: {dados_partida}")
                cursor.execute(query, dados_partida)
                conexao.commit()
                id_gerado = cursor.lastrowid
                print(f'Id gerado Banco: {id_gerado}')

                ids_rodadas_mae.append(id_gerado)
                contador_rodadas+=1
                if(contador_rodadas == 2):
                    lista_id_rodas_mae_anteriores.pop(0)
                    contador_rodadas = 0
                partidas_inseridas += 1
                print(f'Partidas inseridas repeticao: {partidas_inseridas}')
            except mysql.connector.Error as err:
                print(f"Erro ao inserir partida no BD: {err}")
        lista_id_rodas_mae_anteriores.clear()
        lista_id_rodas_mae_anteriores = ids_rodadas_mae
        etapa_atual-=1
    
    print(f'Partidas inseridas Total: {partidas_inseridas}')

    cursor.close()
    conexao.close()

    return partidas_inseridas


def gerarChaveamento(esporte, classificacao):
    
    print(f"--- Gerando Chaveamento para {esporte} ({classificacao}) ---")
    
    # 1. BUSCA AS EQUIPES E INFORMAÇÕES
    # A função buscarEquipesPorModCla deve retornar uma lista de dicionários
    equipes_db = buscarEquipesPorModCla(esporte, classificacao)
    
    if not equipes_db:
        print("Status: Falha. Não há equipes cadastradas ou erro de conexão/consulta.")
        return

    # Extrai o tipo de esporte
    tipo_grupo = equipes_db[0]['grupo'] if equipes_db and 'grupo' in equipes_db[0] else 'Coletivo'
    
    # 2. APLICA A REGRA DE CONFRONTO DE TURMAS
    equipes_para_chavear = []
    equipes_com_info = [{'id': eq['pk_equipe'], 'turma': eq['turma']} for eq in equipes_db]
    
    if tipo_grupo == 'Individual':
        print("Regra: Esporte Individual. Confronto entre turmas permitido.")
        
        # Embaralha todas as equipes, pois não há restrição
        equipes_para_chavear = [eq['id'] for eq in equipes_com_info]
        random.shuffle(equipes_para_chavear)
        
    else: # Esporte Coletivo
        print("Regra: Esporte Coletivo. Tentando evitar confrontos de mesma turma na 1ª Rodada.")
        
        # Agrupa equipes por turma
        turmas_agrupadas = {}
        for eq in equipes_com_info:
            # Garante que usamos a PK e a turma
            turmas_agrupadas.setdefault(eq['turma'], []).append(eq['id'])
            
        # Tenta criar uma lista onde as turmas se alternam para 'espalhar' as equipes
        todas_listas = list(turmas_agrupadas.values())
        
        # Pega uma equipe de cada turma em sequência (até que as listas acabem)
        while any(todas_listas):
            for lista_equipes in todas_listas:
                if lista_equipes:
                    # Usa .pop() para pegar o último ID e remover da lista
                    equipe_escolhida = lista_equipes.pop() 
                    equipes_para_chavear.append(equipe_escolhida)
        
        # Um embaralhamento final suave pode ser feito sem reorganizar muito
        # o que já foi espaçado, mas vamos manter o espalhamento simples por enquanto.


    # 3. GERA O CHAVEAMENTO
    chaveamento = gerar_chaveamento_sem_bye_contra_bye(equipes_para_chavear)
    
    # 4. SALVA NO BANCO DE DADOS
    partidas_salvas = salvar_partidas(chaveamento, esporte, classificacao)
    
    # 5. RELATÓRIO FINAL
    print("\n" + "="*50)
    print(f"CHAVEAMENTO {esporte} ({classificacao}) CONCLUÍDO.")
    print(f"Total de equipes: {len(equipes_db)}")
    print(f"Total de partidas da 1ª rodada salvas no BD: {partidas_salvas}")
    print("="*50 + "\n")
    
    # Imprime o chaveamento (para visualização no console)
    for i, rodada in enumerate(chaveamento):
        print(f"--- Etapa {i + 1} ---")
        for partida in rodada:
            # Partidas da 1ª rodada mostram o ID (int)
            # Partidas futuras mostram o placeholder (str)
            print(f"Partida {partida[0]} vs {partida[1]}")
            
    return chaveamento


# O ponto de execução principal para evitar o RuntimeWarning
if __name__ == "__main__":
    # EXEMPLO DE CHAMADA DE TESTE (Substitua por um esporte real do seu BD)
    # Certifique-se de que a função criarConexao() está funcionando!
    gerarChaveamento('Futsal', 'Masculino')
    # gerarChaveamento('Tênis de Mesa', 'Misto')
    
    # Teste 2: Individual (a regra de turmas NÃO deve ser aplicada)
    # Certifique-se de que 'Tênis de Mesa' existe e está marcado como 'Individual' no seu BD.
    gerarChaveamento('Tênis de Mesa', 'Masculino')