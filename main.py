from flask import Flask, render_template, redirect, request, session, jsonify, flash, url_for
from functools import wraps
from datetime import timedelta, datetime, date
from model import *
from calendar import *

# Assumindo que seu gestao_chaveamento.py está em model/funcoesBD/Chaveamento
# E que o Flask pode importá-lo a partir da raiz 'model'
try:
    from model.funcoesBD.Chaveamento.gestao_chaveamento import gerarChaveamento
except ImportError as e:
    print(f"ATENÇÃO: Falha ao importar gerarChaveamento. Certifique-se de que todas as pastas possuem __init__.py e o caminho está correto. Erro: {e}")
    # Define uma função placeholder para evitar quebra total
    def gerarChaveamento(esporte, classificacao):
        print("!!! FUNÇÃO DE CHAVEAMENTO NÃO CARREGADA !!!")
        return None
 
#Decorator para verificar se o usuario é Administrador
def requerAdmin(f):
    @wraps(f)
    def requerindoAdmin(*args, **kwargs):

        if session['nivel'] != "Administrador":
            return redirect('/')

        if session['nivel'] != "Administrador":
            flash("Faça login como Administrador para ativar esta função.", "error")
            return redirect('/')
        
        return f(*args, **kwargs)
    return requerindoAdmin

#Decorator para verificar se o usuario é Administrador ou AlunoMonitor
def requerAdminOuMonitor(f):
    @wraps(f)
    def requerindo(*args, **kwargs):
        
        if session['nivel'] not in ["Administrador", "AlunoMonitor"]:

            flash("Faça login para ativar esta função.", "warning")
            return redirect('/')
        
        return f(*args, **kwargs)
    return requerindo

def obterAcessoDoUsuario():
    nivel = session.get("nivel", "Visitante")
    turma = session.get("turma")

    if nivel == "Administrador":


        return {
            "nivel": nivel,
            "equipes": buscarEquipes(),
            "turmas": buscarTurmas()
        }

    if nivel == "AlunoMonitor":
        return {
            "nivel": nivel,
            "equipes": buscarEquipesPorTurma(turma),
            "turmas": [{"pk_nome_turma": turma}]
        }

    return {
        "nivel": "Visitante",
        "equipes": buscarEquipes(),
        "turmas": []
    }

app = Flask(__name__)
app.secret_key = '29bfd352-ed9e-4818-b05b-498b8f77e4e3'
app.permanent_session_lifetime = timedelta(days=30)

@app.route("/")
def home():
    nome_usuario = session.get('nome')
    return redirect('/home')


@app.context_processor
def inject_user():
    return dict(nome_usuario=session.get('nome'))


## ---------------LOGIN---------------- ##

# O usuário é considerado visitante se não estiver logado. Criamos uma sessão para ele:

@app.before_request
def criarSessaoVisitante():
    if 'nome' not in session:
        session['nome'] = 'Visitante'
        session['nivel'] = 'Visitante'
        session['turma'] = None

@app.route('/login')
def login():
    if session['nivel'] != 'Visitante':
        return redirect('/')
    else:
        return render_template('login.html')
    
@app.route('/login', methods=['POST'])
def verificarLogin():
    usuario = request.form['usuario']
    senha = request.form['senha']

    # Busca apenas pelo nome do usuário
    usuario_encontrado = buscarUsuarioPorNome(usuario)

    if not usuario_encontrado or senha != usuario_encontrado["senha"]:
        flash('Usuário ou senha estão incorretos.', 'error')
        return redirect(url_for('login'))
    
    # Login bem-sucedido
    session['nome'] = usuario
    session['nivel'] = usuario_encontrado['nivel']

    # Verificação do lembrar_me
    if request.form.get("lembrar_me"):
        session.permanent = True
    else:
        session.permanent = False

    # Verificação do Aluno Monitor
    if usuario_encontrado['nivel'] == 'AlunoMonitor':
        session['turma'] = usuario_encontrado['fk_nome_turma']
    else:
        session['turma'] = None

    return redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/home")
def homeRedirect():
    return render_template("home.html", 
    nome_usuario=session['nome'], 
    nivel=session['nivel'], 
    partidas=buscarPartidas(),
    
    )

## ----------------LISTAGENS----------------- ##

@app.route("/turma")
def turma():
    turmas = buscarTurmas()
    print(turmas[0]['pk_nome_turma'])
    return render_template("turma.html", turmas=turmas)

@app.route("/alunosPorTurma/<turma>")
def alunosPorTurma(turma):
    alunos = buscarAlunosPorTurma(turma)
    # função do model que retorna lista de alunos da turma
    return jsonify({"alunos": [{"matricula": a[0], "nome": a[1]} for a in alunos]})

## ----------------CADASTRAR ALUNOS---------------##

@app.route("/cadastrarAluno", methods=["GET"])
@requerAdminOuMonitor
def paginacadastrarAluno():

    acesso = obterAcessoDoUsuario()

    return render_template(
        "cadastrarAluno.html",
        alunos=buscarAlunos(),
        turmas=buscarTurmas(),
        nivel=acesso["nivel"]
        )

@app.route("/cadastrarAluno", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarAluno():

    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    genero = request.form.get("genero")

    if session['nivel'] == 'Administrador':
        turma = request.form.get("turma")
    else:
        turma = session["turma"]

    cadastrarAluno(matricula, nome, turma, genero)

    return redirect(url_for("paginacadastrarAluno"))

@app.route("/editarAluno/<antiga_matricula>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarAluno(antiga_matricula):

    nome = request.form["nome"]
    genero = request.form["genero"]
    nova_matricula = request.form["nova_matricula"]

    if session["nivel"] == "Administrador":
        turma = request.form["turma"]
    else:
        turma = session["turma"]

    editarAluno(
        nova_matricula,
        nome,
        turma,
        genero,
        antiga_matricula
    )

    return redirect(url_for("paginacadastrarAluno"))

@app.route("/deletarAluno/<matricula>")
@requerAdminOuMonitor
def rotaDeletarAluno(matricula):
    deletarAluno(matricula)
    
    return redirect(url_for("paginacadastrarAluno"))


## ------------------CADASTRAR TURMAS-------------------- ##

# Cadastrar
@app.route("/cadastrarTurma", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarTurma():
    pk_nome_turma = request.form.get("pk_nome_turma")
    icone_url = request.form.get("icone_url") 
    cadastrarTurma(pk_nome_turma, icone_url)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)

# Editar
@app.route("/editarTurma/<string:turma>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarTurma(turma):
    novo_nome = request.form.get("pk_nome_turma")
    icone_url = request.form.get("icone_url") 
    editarTurma(turma, novo_nome, icone_url)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)

# Deletar
@app.route("/deletarTurma/<string:turma>")
@requerAdminOuMonitor
def rotaDeletarTurma(turma):
    deletarTurma(turma)
    turmas = buscarTurmas()
    return render_template("turma.html", turmas=turmas)


## ---------------------CADASTRAR EQUIPE---------------------- ##

@app.route("/cadastrarEquipe", methods=["GET"])
def paginaCadastrarEquipe():

    acesso = obterAcessoDoUsuario()

    return render_template(
        "cadastrarEquipe.html",
        equipes=acesso["equipes"],
        turmas=acesso["turmas"],
        esportes = buscarEsportes(),
        classificacoes = buscarClassificacoes(),
        nivel=acesso["nivel"],
        prazo_edicao=buscarConfiguracao("prazo_edicao_equipes")
    )


@app.route("/cadastrarEquipe", methods=["POST"])
@requerAdminOuMonitor
def rotaCadastrarEquipe():
    esporte = request.form.get("esporte")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    alunos = request.form.getlist("alunos")

    cadastrarEquipe(esporte, turma, genero, alunos)
    flash("Equipe cadastrada com sucesso.", "success")

    return redirect("/cadastrarEquipe")

@app.route("/editarEquipe/<int:pk_equipe>", methods=["POST"])
@requerAdminOuMonitor
def rotaEditarEquipe(pk_equipe):

    if not edicaoEquipesPermitida():
        flash("O prazo para editar equipes foi encerrado.", "error")
        return redirect("/cadastrarEquipe")

    esporte = request.form.get("esporte")
    turma = request.form.get("turma")
    genero = request.form.get("genero")
    alunos = request.form.getlist("alunos")

    editarEquipe(pk_equipe, esporte, turma, genero, alunos)

    flash("Equipe editada com sucesso.", "success")
    return redirect("/cadastrarEquipe")

@app.route("/alterarPrazoEdicao", methods=["POST"])
@requerAdmin
def alterarPrazo():

    prazo = request.form.get("prazo")

    alterarConfiguracao(
        "prazo_edicao_equipes",
        prazo
    )

    flash("Prazo atualizado com sucesso!", "success")

    return redirect(url_for("paginaCadastrarEquipe"))

#Deletar equipe
@app.route("/deletarEquipe/<int:pk_equipe>")
@requerAdminOuMonitor
def rotaDeletarEquipe(pk_equipe):
    resultado = deletarEquipe(pk_equipe)
    flash("Equipe deletada com sucesso.", "success")
    return resultado  # retorna texto direto pro fetch()


# Buscar alunos por turma (JSON)
@app.route("/alunosPorTurma/<nome_turma>/<classificacao>")
def alunosPorTurmaEquipes(nome_turma, classificacao):
    alunos = alunosPorTurmaListaEquipes(nome_turma, classificacao)
    return jsonify({"alunos": alunos})

# Jogadores de uma equipe (JSON)
@app.route("/jogadoresPorEquipe/<int:id_equipe>")
def jogadoresPorEquipe(id_equipe):
    jogadores = buscarJogadoresPorEquipe(id_equipe)
    return jsonify({"jogadores": jogadores})


## -------------------CADASTRO DO USUARIO------------------ ##

# Página de cadastro
@app.route("/cadastrarUsuario", methods=["GET"])
def paginaCadastrarUsuario():
    usuarios = telaUsuarios()
    turmas = buscarTurmas()
    return render_template("cadastrarUsuario.html", usuarios=usuarios, turmas=turmas)

# Inserção no banco
@app.route("/cadastrarUsuario", methods=["POST"])
def rotaCadastrarUsuario():
    pk_usuario = request.form.get("pk_usuario")
    senha = request.form.get("senha")
    nivel = request.form.get("nivel")
    fk_nome_turma = request.form.get("fk_nome_turma") if nivel == "AlunoMonitor" else None

        #--Validação: aluno monitor precisa de turma
    if nivel == "AlunoMonitor" and (not fk_nome_turma or fk_nome_turma.strip() == ""):
        flash("Erro: Aluno Monitor precisa estar vinculado a uma turma.", "error")
        return redirect(url_for("paginaCadastrarUsuario"))


    try:

        cadastrarUsuario(pk_usuario, senha, nivel, fk_nome_turma)
        flash("Usuário cadastrado com sucesso!", "success")

    except Exception as e:
        flash("O nome de usuário que você tentou cadastrar já existe.\n" "Por favor, tente outro.", "error")

    return redirect(url_for("paginaCadastrarUsuario"))

# Edição
@app.route("/editarUsuario/<pk_usuario>", methods=["POST"])
def rotaEditarUsuario(pk_usuario):
    novo_usuario = request.form.get("pk_usuario")
    senha = request.form.get("senha")  # opcional
    nivel = request.form.get("nivel")
    fk_nome_turma = request.form.get("fk_nome_turma") if nivel == "AlunoMonitor" else None

    #--Validação
    if nivel == "AlunoMonitor" and (not fk_nome_turma or fk_nome_turma.strip() == ""):
        flash("Erro: Aluno Monitor precisa estar vinculado a uma turma.", "error")
        return redirect(url_for("paginaCadastrarUsuario"))

    editarUsuario(pk_usuario, novo_usuario, senha, nivel, fk_nome_turma)
    flash("Usuário atualizado com sucesso!", "success")
    return redirect(url_for("paginaCadastrarUsuario"))

# Deleção
@app.route("/deletarUsuario/<pk_usuario>")
def rotaDeletarUsuario(pk_usuario):
    deletarUsuario(pk_usuario)
    usuarios = telaUsuarios()
    turmas = buscarTurmas()
    return render_template("cadastrarUsuario.html", usuarios=usuarios, turmas=turmas)


## ----------------GERENCIAR/CADASTRAR MODALIDADES------------------ ##

@app.route("/gerenciarModalidades")
def gerenciarModalidades():
    esportes = buscarEsportes()
    return render_template("gerenciarModalidades.html", esportes=esportes)

#Cadastra modalidade juntamente com a classificação dela (Individual, Coletivo) e Quantidade de jogadores
@app.route('/cadastrarModalidades', methods=['POST'])
@requerAdmin
def processarCadastroModalidades():
    esporte = request.form['esporte']
    esporte = esporte.title()
    grupo = request.form['grupo']
    qtdJogadores = request.form['qtdJogadores']
    cadastrarEsportes(esporte, grupo, qtdJogadores)
    return redirect('/gerenciarModalidades')


## ----------------CALENDÁRIO------------------ ##

@app.route('/calendario')
@app.route('/calendario/<int:ano>/<int:mes>')
@app.route('/calendario/<int:ano>/<int:mes>/<int:dia>')
def calendario(ano = None, mes = None, dia = None):
    # Lógica para obter o ano, mês e dia atuais caso não sejam fornecidos na URL
    #Parâmetros:
    #- ano (int): O ano para exibição do calendário. Se não fornecido, é o ano atual.
    #- mes (int): O mês para exibição do calendário. Se não fornecido, é o mês atual.
    #- dia (int): O dia selecionado. Se não fornecido, é o dia atual.
    if ano is None or mes is None:
        hoje = datetime.today()
        ano = hoje.year
        mes = hoje.month
    
    if dia is None:
        dia_selecionado = datetime.today().day
    else:
        dia_selecionado = dia
    
    # Ajuste de mês e ano caso o usuário navegue para meses anteriores ou seguintes:
    #Se o mes for igual a 0, significa que o usuario foi para o ano anterior, ou seja, mês se torna igual a 12 e ano = ano atual - 1
    #Se o mes for igual a 13, significa que o usuario foi para o ano posterior, ou seja, mês se torna igual a 1 e ano = ano atual + 1
    if mes == 0:
        mes = 12
        ano -=1
    elif mes == 13:
        mes = 1
        ano += 1

    turmas = buscarTurmas()

    #Busca eventos no calendario do mês de determinado ano    
    eventos = buscarEventosCalendario(ano, mes)
    eventosDoDia = set() #Evita que tenha duplicatas, pois apenas registra em quais dias tem partidas
    for evento in eventos:
        eventosDoDia.add(evento['dia_evento'].day)

    #Procura as partidas do dia que o usuário escolheu no calendário
    partidas_dia_selecionado = []
    for partida in eventos:
        if partida['dia_evento'].day == dia_selecionado:
            partidas_dia_selecionado.append(partida)

    #Define domingo como o primeiro dia da semana
    calendario_mes = Calendar(firstweekday=6)
    #Busca as semanas do mês de determinado ano
    semanas = calendario_mes.monthdatescalendar(ano, mes) 
    
    #Armazena os nomes dos meses para ser exibido no calendario
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    #nomeMes recebe meses[mes(numero do mês) - 1], pois em listas o primeiro indíce de uma lista é 0
    nomeMes = meses[mes - 1]

    #Funções necessárias para exibição do usuário
    membrosEquipes = buscarMembrosEquipe()
    esportes = buscarEsportes()
    estatisticasPrincipal = buscarEstatisticasPrincipal()

    return render_template('calendario.html', 
        ptr = partidas_dia_selecionado,  
        turmas = turmas,
        hoje = date.today(),
        ano = ano,
        semanas = semanas,
        mes = mes,
        eventosDoDia = eventosDoDia,
        nomeMes = nomeMes,
        membrosEquipes = membrosEquipes,
        esportes = esportes,
        dia_selecionado = dia_selecionado,
        estatisticasPrincipal = estatisticasPrincipal)

#Rota necessária para a função de filtrar informações no calendário
@app.route('/calendarioFiltrado/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
def calendarioFiltrado(ano = None, mes = None, dia = None):
    esporte = request.form['esporte']
    genero = request.form['genero']
    turma = request.form['turma']

    if ano is None or mes is None:
        hoje = datetime.today()
        ano = hoje.year
        mes = hoje.month
    
    if dia is None:
        dia_selecionado = datetime.today().day
    else:
        dia_selecionado = dia
    
    if mes == 0:
        mes = 12
        ano -=1
    elif mes == 13:
        mes = 1
        ano += 1

    turmas = buscarTurmas()
    
    #Busca eventos de maneira especifica, conforme esporte e/ou turma e/ou genero -- OBS: Genero = Masculino ou Feminino
    eventos = buscarEventosCalendarioFiltros(ano, mes, esporte, turma, genero)
    eventosDoDia = set()
    for evento in eventos:
        eventosDoDia.add(evento['dia_evento'].day)

    partidas_dia_selecionado = []
    for partida in eventos:
        if partida['dia_evento'].day == dia_selecionado:
            partidas_dia_selecionado.append(partida)
    
    calendario_mes = Calendar(firstweekday=6)
    semanas = calendario_mes.monthdatescalendar(ano, mes) 
    
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    nomeMes = meses[mes - 1]

    membrosEquipes = buscarMembrosEquipe()
    esportes = buscarEsportes()
    estatisticasPrincipal = buscarEstatisticasPrincipal()

    return render_template('calendario.html', 
        ptr = partidas_dia_selecionado,  
        turmas = turmas,
        hoje = date.today(),
        ano = ano,
        semanas = semanas,
        mes = mes,
        eventosDoDia = eventosDoDia,
        nomeMes = nomeMes,
        membrosEquipes = membrosEquipes,
        esportes = esportes,
        dia_selecionado = dia_selecionado,
        filtroEsporte = esporte,
        filtroGenero= genero,
        filtroTurmas = turma,
        estatisticasPrincipal = estatisticasPrincipal)

## ----------------TABELA ATLETISMO------------------ ##

@app.route("/tabelaAtletismo", methods=["GET"])
def tabelaAtletismo():
    return render_template(
        "tabelaAtletismo.html",
        esportes=buscarEsportes(),
        classificacoes=buscarClassificacoes()
    )

# =========================================================
# TABELA DO ATLETISMO - MODALIDADES
# =========================================================

@app.route("/tabelaAtletismo/Modalidades", methods=["GET"])
def tabelaAtletismoModalidade():
    return render_template(
        "tabelaAtletismoModalidade.html",
        modalidades=buscarModalidadesAtletismo()
    )


# =========================================================
# TABELA DO ATLETISMO - RECORDES
# =========================================================

@app.route("/tabelaAtletismo/Recordes", methods=["GET"])
def tabelaAtletismoRecordes():
    return render_template(
        "tabelaAtletismoRecordes.html"
    )

# =========================================================
# TABELA DO ATLETISMO - PROVAS
# =========================================================

@app.route("/tabelaAtletismo/Provas", methods=["GET"])
def tabelaAtletismoProvas():

    return render_template(

        "tabelaAtletismoProvas.html",

    )

## ----------------CHAVEAMENTO------------------ ##

@app.route("/gerarChaveamento", methods=["GET"])
def paginaGerarChaveamento():
    # Buscar esportes e classificações para preencher os <select> no HTML
    esportes = buscarEsportes()
    classificacoes = buscarClassificacoes()
    
    return render_template(
        "gerarChaveamento.html", 
        esportes=esportes, 
        classificacoes=classificacoes
    )


@app.route("/chaveamento/gerar", methods=["POST"])
@requerAdmin
def rotaGerarChaveamento():
    dados = request.get_json() or {}
    esporte = dados.get('esporte')
    classificacao = dados.get('classificacao')

    if not esporte or not classificacao:
        return jsonify({"status": "erro", "mensagem": "Esporte e Classificação são obrigatórios."}), 400

    # Redirecionamento dinâmico enviado para o Fetch/AJAX do Javascript
    if esporte == "Atletismo":
        return jsonify({
            "status": "redirecionar",
            "url": url_for("tabelaAtletismo")
        })

    try:
        chaveamento = gerarChaveamento(esporte, classificacao) 
        total_partidas_1a_rodada = len(chaveamento[0]) if chaveamento and chaveamento[0] else 0

        return jsonify({
            "status": "sucesso",
            "mensagem": f"Chaveamento de {esporte} ({classificacao}) gerado e salvo.",
            "total_partidas": total_partidas_1a_rodada
        })

    except Exception as e:
        print(f"Erro Crítico ao Gerar Chaveamento: {e}")
        return jsonify({
            "status": "erro", 
            "mensagem": f"Erro interno ao gerar chaveamento: {str(e)}"
        }), 500
    
@app.route("/chaveamento/partidas", methods=["GET"])
def rotaBuscarPartidas():
    """
    Busca as partidas de uma chave (filtrada por GET) para listagem no painel.
    """
    # Recebe os filtros do JavaScript via URL params (request.args)
    esporte = request.args.get('esporte')
    classificacao = request.args.get('classificacao')
    
    if not esporte and not classificacao:
        return jsonify({"status": "erro", "mensagem": "Filtros são obrigatórios para buscar partidas."}), 400

    try:
        # 1. Busca no BD a lista completa de partidas da chave (com nomes das equipes)
        partidas_bd = buscarPartidasParaGestao(esporte, classificacao) 
        print(partidas_bd)

        # 2. Prepara o JSON para o frontend
        partidas_json = []
        for p in partidas_bd:
            # Assumimos que a função de busca (buscarPartidasParaGestao) já traz 'pk_equipe_vencedora'
            partidas_json.append({
                "pk_partida": p['pk_partida'],
                "esporte": p['fk_esporte'],
                "classificacao": p['fk_genero'],
                "etapa": p['etapa'],
                "fk_equipe_casa": p['fk_equipe_casa'],
                "equipe_casa_nome": p['nome_equipe_casa'],
                "fk_equipe_visitante": p['fk_equipe_visitante'],
                "equipe_visitante_nome": p['nome_equipe_visitante'],
                "vencedor_pk": p.get('pk_equipe_vencedora')
            })

        return jsonify({"status": "sucesso", "partidas": partidas_json})

    except Exception as e:
        print(f"Erro ao buscar partidas: {e}")
        return jsonify({"status": "erro", "mensagem": "Falha ao carregar partidas do banco de dados."}), 500


@app.route("/chaveamento", methods=['GET', 'POST'])
def chaveamentoTeste():
    esportes = buscarEsportes()
    generos = buscarClassificacoes()

    tabela = None  # Inicializa a tabela como None
    esporte = None
    genero = None

    if request.method == 'POST':
        esporte = request.form['esporte']
        genero = request.form['genero']

        if esporte == "Atletismo":
            return redirect(url_for("tabelaAtletismo"))

        if esporte and genero:
            tabela = buscarPartidasParaGestao(esporte, genero)

    return render_template("chaveamento.html", esportes=esportes, generos=generos, tabela=tabela)

@app.route("/chaveamento/vencedor", methods=["POST"])
@requerAdmin
def rotaRegistrarVencedor():
    partida_id = request.form['partida_id']
    cod_partida_mae = request.form.get('cod_partida_mae')

    cod_equipe_casa = request.form['cod_equipe_casa']
    cod_equipe_visitante = request.form['cod_equipe_visitante']

    pontos_equipe_casa = int(request.form['pontos_equipe_casa'])
    pontos_equipe_visitante = int(request.form['pontos_equipe_visitante'])

    genero = request.form['genero']
    esporte = request.form['esporte']

    vencedor_id = (
        cod_equipe_casa
        if pontos_equipe_casa > pontos_equipe_visitante
        else cod_equipe_visitante
    )

    salvarVencedorPartida(
        partida_id,
        vencedor_id,
        pontos_equipe_casa,
        pontos_equipe_visitante,
        cod_partida_mae
    )

    tabela = buscarPartidasParaGestao(esporte, genero)
    esportes = buscarEsportes()
    generos = buscarClassificacoes()

    return render_template(
        "chaveamento.html",
        esportes=esportes,
        generos=generos,
        tabela=tabela
    )

@app.route('/gerenciarEstatisticas')
@requerAdmin
def exibirGerenciarEstatisticas():
    esportes = buscarModalidades()
    estatisticas = buscarEstatisticasRegistradas()
    esportesComEst = buscarEstatisticasDeModalidade()
    return render_template('gerenciarEstatisticas.html', esportes=esportes, estatisticas=estatisticas, esportesComEst=esportesComEst)

@app.route('/criarEstatistica', methods=['POST'])
@requerAdmin
def processarCriarEstatistica():
    estatistica = request.form['estatistica']
    estatistica = estatistica.title()
    criarEstatisticas(estatistica)
    return redirect(f'/gerenciarEstatisticas')

@app.route('/removerEstatistica', methods=['POST'])
@requerAdmin
def processarRemoverEstatistica():
    estatistica = request.form['estatistica']
    removerEstatisticas(estatistica)
    return redirect(f'/gerenciarEstatisticas')

@app.route("/cadastrarEstatisticasParaModalidade", methods=['POST'])
def processarCadastrarEstatisticaModalidade():
    esporte = request.form['esporte']
    estatistica = request.form['estatistica']
    cadastrarEstatisticasParaModalidade(esporte, estatistica)
    return redirect(f'/gerenciarEstatisticas')

#Remove estatistica de determinada modalidade
@app.route("/removerEstatisticasParaModalidade", methods=["POST"])
@requerAdmin
def processarRemoverEstatisticaModalidade():
    esporte = request.form['esporte']
    estatistica = request.form['estatistica']
    if esporte == '':
        flash('Selecione um esporte valido!', 'erro')
    else:
        removerEstatisticasDaModalidade(esporte,estatistica)
    return redirect(f'/gerenciarEstatisticas')

#API relacionada a tela de gerenciar estatisticas na função remover estatisticas para modalidade
@app.route('/api/estatisticasPorModalidade/<string:esporte>')
def processarEstatisticasPorModalidade(esporte):
    estatisticasFiltras = buscarEstatisticasPorModalidade(esporte)
    return jsonify(estatisticasFiltras)