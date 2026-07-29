import logging
import os
import re

os.makedirs("logs", exist_ok=True)

OPERACOES = {
    "SELECT":"Consultou",
    "INSERT":"Cadastrou",
    "UPDATE":"Atualizou",
    "DELETE":"Deletou"
}

TABELAS = {
    "alunos":"Aluno(a)",
    "equipes":"Equipe",
    "estatisticas_esporte":"Estatistica Esportiva",
    "esportes":"Esporte",
    "partidas":"Chaveamento",
    "login":"Usuario",
    "turmas":"Turma"

}

def criarLOGInfo(query, usuario_logado, usuario_cadastrado=None):
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/Sistema.log",
    encoding="utf-8"
    )

    operacao = query.split()[0].upper()

    match = re.search(r"(?:FROM|INTO|UPDATE)\s+(\w+)", query, re.IGNORECASE)
    tabela = match.group(1) if match else None
    nome_tabela = TABELAS.get(tabela, tabela)

    logger = logging.getLogger("Sistema")

    acao = OPERACOES.get(operacao, operacao)

    if acao == "Consultou":
        logger.info("%s %s os %s", usuario_logado, acao, nome_tabela)
    elif acao == "Cadastrou":
        if tabela == "alunos":
            logger.info("%s %s um(a) %s", usuario_logado, acao, nome_tabela)
        elif tabela == "equipes" or tabela == "turmas" or tabela == "estatisticas_esporte":
            logger.info("%s %s uma %s", usuario_logado,acao,nome_tabela)
        elif tabela == "esportes":
            logger.info("%s %s um %s", usuario_logado, acao, nome_tabela)
        elif tabela == "login":
            logger.info("%s %s o usuário %s", usuario_logado, acao, usuario_cadastrado)

criarLOGInfo("Select * from alunos", "adm")