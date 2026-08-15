from flask import Flask, render_template, redirect, request, session, jsonify, flash, url_for
from functools import wraps
from datetime import timedelta, datetime, date
from model import *
from calendar import *

print("Main iniciado")
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

    partidas = buscarPartidasDoDia()

    return render_template(
        "home.html",
        nome_usuario=session.get("nome", "Visitante"),
        nivel=session.get("nivel", "Visitante"),
        partidas=partidas
    )

## ----------------ATLETISMO----------------- ##

@app.route("/tabelaAtletismo", methods=["GET", "POST"])
def tabelaAtletismo():
    if request.method == "GET":
            return render_template("tabelaAtletismo.html")


# =========================================================
# TABELA DO ATLETISMO - MODALIDADES
# =========================================================

@app.route("/tabelaAtletismo/Modalidades", methods=["GET", "POST"])
@requerAdmin
def tabelaAtletismoModalidade():

    # =====================================================
    # GET - EXIBIR MODALIDADES
    # =====================================================

    if request.method == "GET":

        dados = buscarModalidades()

        modalidades = dados["modalidades_atletismo"]

        return render_template(
            "tabelaAtletismoModalidade.html",
            modalidades=modalidades
        )


    # =====================================================
    # POST
    # =====================================================

    elif request.method == "POST":

        dados = request.get_json(silent=True)

        if dados is None:
            dados = request.form


        # =================================================
        # DADOS RECEBIDOS
        # =================================================

        acao = dados.get("acao")

        pk_modalidade = dados.get("pk_modalidade")
        nome_modalidade = dados.get("nome_modalidade")
        descricao = dados.get("descricao")
        ativo = dados.get("ativo", 1)


        # =================================================
        # EXCLUSÃO
        # =================================================

        if acao == "deletar":

            if not pk_modalidade:

                return jsonify({
                    "status": "erro",
                    "mensagem": "Modalidade não informada."
                }), 400


            try:

                deletarModalidadeAtletismo(
                    pk_modalidade
                )

                return jsonify({
                    "status": "sucesso",
                    "mensagem": "Modalidade excluída com sucesso."
                })


            except Exception as erro:

                print(
                    f"Erro ao excluir modalidade: {erro}"
                )

                return jsonify({
                    "status": "erro",
                    "mensagem": (
                        "Não foi possível excluir a modalidade."
                    )
                }), 500


        # =================================================
        # VALIDAÇÃO - CADASTRO / EDIÇÃO
        # =================================================

        if not nome_modalidade:

            return jsonify({
                "status": "erro",
                "mensagem": "O nome da modalidade é obrigatório."
            }), 400


        try:

            # =============================================
            # EDIÇÃO
            # =============================================

            if pk_modalidade:

                editarModalidadeAtletismo(
                    pk_modalidade,
                    nome_modalidade,
                    descricao,
                    ativo
                )

                return jsonify({
                    "status": "sucesso",
                    "mensagem": (
                        f"Modalidade '{nome_modalidade}' "
                        "atualizada com sucesso."
                    )
                })


            # =============================================
            # CADASTRO
            # =============================================

            else:

                novo_id = cadastrarModalidadeAtletismo(
                    nome_modalidade,
                    descricao,
                    ativo
                )

                return jsonify({
                    "status": "sucesso",
                    "mensagem": (
                        f"Modalidade '{nome_modalidade}' "
                        "cadastrada com sucesso."
                    ),
                    "pk_modalidade": novo_id
                })


        except Exception as erro:

            print(
                f"Erro ao processar modalidade: {erro}"
            )

            return jsonify({
                "status": "erro",
                "mensagem": (
                    f"Erro interno ao processar modalidade: {str(erro)}"
                )
            }), 500


@app.route("/tabelaAtletismo/Provas", methods=["GET", "POST"])
def tabelaAtletismoProvas():

    # =========================
    # CADASTRAR NOVA PROVA (POST)
    # =========================
    if request.method == "POST":
        fk_modalidade = request.form.get("fk_modalidade")
        fk_genero = request.form.get("fk_genero")
        nome_prova = request.form.get("nome_prova")
        tipo_resultado = request.form.get("tipo_resultado")
        unidade_medida = request.form.get("unidade_medida")
        data_hora = request.form.get("data_hora")

        if not (fk_modalidade and fk_genero and nome_prova and tipo_resultado and unidade_medida):
            flash("Preencha todos os campos obrigatórios.", "error")
            return redirect(url_for("tabelaAtletismoProvas"))

        try:
            cadastrarProvaAtletismo(
                fk_modalidade,
                fk_genero,
                nome_prova,
                tipo_resultado,
                unidade_medida,
                data_hora if data_hora else None
            )
            flash("Prova cadastrada com sucesso!", "success")
        except Exception as erro:
            print("ERRO AO CADASTRAR PROVA:", erro)
            flash("Erro ao cadastrar a prova.", "error")

        return redirect(url_for("tabelaAtletismoProvas"))

    # =========================
    # CARREGAR PÁGINA (GET)
    # =========================
    dadosAtletismo = buscarModalidades()

    # (OPCIONAL) Crie ou importe essa função para buscar os alunos cadastrados
    alunos = buscarAlunos() 

    return render_template(
        "tabelaAtletismoProvas.html",
        provas=buscarProvas(),
        provasProximas=buscarProvasProximas(),
        modalidades=dadosAtletismo["modalidades_atletismo"],
        generos=buscarClassificacoes(),
        alunos=alunos  # <--- Passando a lista de alunos para o template
    )

@app.route("/tabelaAtletismo/Provas/Inscrever", methods=["POST"])
def inscreverAtletaProva():
    fk_prova = request.form.get("fk_prova")
    fk_matricula = request.form.get("fk_matricula")

    if not fk_prova or not fk_matricula:
        flash("Selecione um atleta para inscrever.", "error")
        return redirect(url_for("tabelaAtletismoProvas"))

    try:
        # Função no seu Model para inserir na tabela associativa
        cadastrarAtletaAtletismo(fk_prova, fk_matricula) 
        flash("Atleta inscrito com sucesso!", "success")
    except Exception as erro:
        print("ERRO AO INSCREVER ATLETA:", erro)
        flash("Este atleta já está inscrito nesta prova ou ocorreu um erro.", "error")

    return redirect(url_for("tabelaAtletismoProvas"))

@app.route("/tabelaAtletismo/Provas/AlterarStatus", methods=["POST"])
def alterarStatusProva():
    fk_prova = request.form.get("fk_prova")
    novo_status = request.form.get("status") # Ex: 'em_andamento', 'finalizada'

    if fk_prova and novo_status:
        try:
            conexao = criarConexao()
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE provas_atletismo SET status = %s WHERE pk_prova = %s",
                (novo_status, fk_prova)
            )
            conexao.commit()
            cursor.close()
            conexao.close()
            flash("Status da prova atualizado!", "success")
        except Exception as e:
            print("Erro ao atualizar status:", e)
            flash("Erro ao atualizar status da prova.", "error")

    return redirect(url_for("tabelaAtletismoProvas"))

@app.route("/tabelaAtletismo/Provas/Deletar", methods=["POST"])
@requerAdmin
def deletarProvaAtletismoRota():

    pk_prova = request.form.get("pk_prova")

    if not pk_prova:
        flash("Prova não informada.", "error")
        return redirect(url_for("tabelaAtletismoProvas"))

    try:

        deletarProvaAtletismo(pk_prova)

        flash("Prova excluída permanentemente.", "success")

    except Exception as erro:

        print("ERRO AO EXCLUIR PROVA:", erro)

        flash(
            "Não foi possível excluir a prova.",
            "error"
        )

    return redirect(url_for("tabelaAtletismoProvas"))

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

    usuario_logado = session["nome"]

    cadastrarAluno(matricula, nome, turma, genero, usuario_logado)

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
    cadastrarTurma(pk_nome_turma, icone_url, session["nome"])
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
    usuario_logado = session["nome"]

    cadastrarEquipe(esporte, turma, genero, alunos, usuario_logado)
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
    esportes = buscarEsportes()
    estatisticas = buscarEstatisticasDasModalidades()
    return render_template("cadastrarUsuario.html", 
    usuarios=usuarios, 
    turmas=turmas, 
    esportes=esportes, 
    estatisticas=estatisticas,
    )

# Inserção no banco
@app.route("/cadastrarUsuario", methods=["POST"])
def rotaCadastrarUsuario():
    pk_usuario = request.form.get("pk_usuario")
    senha = request.form.get("senha")
    nivel = request.form.get("nivel")
    fk_nome_turma = request.form.get("fk_nome_turma") if nivel == "AlunoMonitor" else None
    esporte = request.form.get("fk_esporte")
    estatistica = request.form.get("fk_estatistica")

    usuario_logado = session["nome"]

        #--Validação: aluno monitor precisa de turma
    if nivel == "AlunoMonitor" and (not fk_nome_turma or fk_nome_turma.strip() == ""):
        flash("Erro: Aluno Monitor precisa estar vinculado a uma turma.", "error")
        return redirect(url_for("paginaCadastrarUsuario"))


    try:

        cadastrarUsuario(pk_usuario, senha, nivel, usuario_logado, fk_nome_turma, esporte, estatistica)
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
    return redirect(url_for("paginaCadastrarUsuario"))


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

@app.route('/removerModalidades', methods=['POST'])
@requerAdmin
def apagarModalidade():
    esporte = request.form['esporte'].title()
    removerModalidade(esporte)
    return redirect('/gerenciarModalidades')


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

@app.route("/verEstatisticas/<int:partida_id>", methods=["GET"])
def verEstatisticas(partida_id):
    partida = buscarPartidaPorId(partida_id)

    esporte = partida["fk_esporte"]
    fk_equipe_casa = partida["fk_equipe_casa"]
    fk_equipe_visitante = partida["fk_equipe_visitante"]
    definida = partida["definida"]
    nivel = session["nivel"]
    equipe_casa = None
    equipe_visitante = None

    if fk_equipe_casa is not None and fk_equipe_visitante is not None:
        equipes = buscarEquipesPorID(fk_equipe_casa, fk_equipe_visitante)
        equipe_casa = equipes[0]
        equipe_visitante = equipes[1]
    else:
        redirect(url_for('chaveamentoTeste'))
    
    estatisticasList = buscarEstatisticasPorModalidade(esporte)
    estatisticas = []
    for estatistica, principal in estatisticasList:
        if principal == 1:
            estatisticas.insert(0, estatistica)
        else:
            estatisticas.append(estatistica)

    usuario = buscarUsuarioPorNome(session["nome"])
    if usuario != None:
        estatistica_permitida = usuario["fk_estatistica_permitida"]
    
    if nivel == "AlunoMonitor":
        estatisticas = [estatistica_permitida]

    estatisticas_partida = buscarEstatisticasDasPartidas(partida_id)


    return render_template("verEstatisticas.html", 
    esporte=esporte, 
    equipe_casa=equipe_casa, 
    equipe_visitante=equipe_visitante,
    fk_equipe_casa=fk_equipe_casa,
    fk_equipe_visitante=fk_equipe_visitante,
    id_partida=partida_id,
    estatisticas=estatisticas,
    definida=definida,
    nivel=nivel,
    estatisticas_partida=estatisticas_partida
    )

@app.route("/salvarEstatisticas", methods=["POST"])
@requerAdminOuMonitor
def salvarEstatisticas():
    try:
        dados = request.get_json()
        modo_edicao = dados.get('modo_edicao')

        id_partida = dados.get("id_partida")
        estatisticas = dados.get("estatisticas", [])

        modalidade = buscarEsportePorPartida(id_partida)
        estatistica_principal = buscarEstatisticasPrincipal(modalidade)
        partida = buscarPartidaPorId(id_partida)

        cod_partida_mae = partida["pk_partida_mae"]
        cod_equipe_casa = partida["fk_equipe_casa"]
        cod_equipe_visitante = partida["fk_equipe_visitante"]

        vencedor_id = None
        pontos_equipe_casa = 0
        pontos_equipe_visitante = 0

        ponto_principal_casa = 0
        ponto_principal_visitante = 0

        for stat in estatisticas:

            nome_estatistica = stat.get("estatistica")
            pontos_equipe_casa = int(stat.get("casa", 0))
            pontos_equipe_visitante = int(stat.get("visitante", 0))

            salvarOuAtualizarEstatistica(id_partida, nome_estatistica, pontos_equipe_casa, pontos_equipe_visitante)


            if nome_estatistica == estatistica_principal:

                ponto_principal_casa = pontos_equipe_casa
                ponto_principal_visitante = pontos_equipe_visitante

                vencedor_id = (
                    cod_equipe_casa
                    if ponto_principal_casa > ponto_principal_visitante
                    else cod_equipe_visitante
                )

        if vencedor_id is None:

            print("ERRO: vencedor_id continua None")

            return jsonify({
                "sucesso": False,
                "mensagem": (
                    "A estatística principal não foi encontrada. "
                    f"Recebida: {estatistica_principal}"
                )
            }), 400

        salvarVencedorPartida(
            id_partida,
            vencedor_id,
            ponto_principal_casa,
            ponto_principal_visitante,
            cod_partida_mae,
            modo_edicao
        )

        return jsonify({
            "sucesso": True,
            "mensagem": "Estatísticas salvas com sucesso"
        }), 200

    except Exception as e:

        import traceback

        print("\n========== ERRO ==========")
        print("TIPO:", type(e).__name__)
        print("MENSAGEM:", str(e))
        traceback.print_exc()
        print("===========================\n")

        return jsonify({
            "sucesso": False,
            "mensagem": f"{type(e).__name__}: {str(e)}"
        }), 500

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
        cod_partida_mae,
        
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
    principal = request.form.get("estatistica_principal") == "true"
    cadastrarEstatisticasParaModalidade(esporte, estatistica, principal)
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
    resultado = [{"fk_nome_estatistica": linha[0]} for linha in estatisticasFiltras]
    return jsonify(resultado)

#---------------- CALENDÁRIO ------------------#

@app.route('/calendarioteste')
def calendarioteste():

    podeEditar = session.get('nivel') in [
        'Administrador',
        'AlunoMonitor'
    ]

    return render_template(
    'calendario2.html',
    podeEditar=podeEditar

    )


# =====================================================
# EVENTOS DO CALENDÁRIO
# =====================================================
@app.route('/calendario/eventos')
def eventosCalendario():

    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                c.pk_evento,
                c.dia_evento,
                c.hora_inicio,
                c.hora_fim,

                p.fk_esporte,
                p.fk_genero,
                p.etapa,

                ec.fk_nome_turma AS turma_casa,
                ev.fk_nome_turma AS turma_visitante

            FROM calendario c

            INNER JOIN partidas p
                ON c.fk_partida = p.pk_partida

            INNER JOIN equipes ec
                ON p.fk_equipe_casa = ec.pk_equipe

            INNER JOIN equipes ev
                ON p.fk_equipe_visitante = ev.pk_equipe

            ORDER BY
                c.dia_evento,
                c.hora_inicio
        """)

        cores = {
            'Vôlei': '#1976d2',
            'Futsal': '#111111',
            'Basquete': '#f57c00',
            'Handebol': '#d32f2f',
            'Queimada': '#2e7d32',
            'Xadrez': '#6a1b9a',
            'Tênis de Mesa': '#c9a227'
        }

        etapas = {
            1: 'Rodada 1',
            2: 'Rodada 2',
            3: 'Rodada 3',
            4: 'Rodada 4'
        }

        eventos = []

        for e in cursor.fetchall():

            turma_casa = e['turma_casa']
            turma_visitante = e['turma_visitante']

            turmas = [
                turma
                for turma in [
                    turma_casa,
                    turma_visitante
                ]
                if turma
            ]

            cor = cores.get(
                e['fk_esporte'],
                '#3788d8'
            )

            # Texto claro para fundos escuros
            # e escuro para fundos claros.
            if e['fk_esporte'] in [
                'Vôlei',
                'Futsal',
                'Handebol',
                'Xadrez'
            ]:
                texto = '#ffffff'
            else:
                texto = '#122f4a'

            eventos.append({

                'id':
                    str(e['pk_evento']),

                'title':
                    f"{turma_casa or 'Turma não informada'} × "
                    f"{turma_visitante or 'Turma não informada'}",

                'start':
                    f"{e['dia_evento']}T"
                    f"{e['hora_inicio']}",

                'end':
                    f"{e['dia_evento']}T"
                    f"{e['hora_fim']}",

                'backgroundColor':
                    cor,

                'borderColor':
                    cor,

                'textColor':
                    texto,

                'extendedProps': {

                    'esporte':
                        e['fk_esporte'],

                    'genero':
                        e['fk_genero'],

                    'etapa':
                        etapas.get(
                            e['etapa'],
                            f"Rodada {e['etapa']}"
                        ),

                    'turma_casa':
                        turma_casa,

                    'turma_visitante':
                        turma_visitante,

                    'turmas':
                        turmas
                }
            })

        return jsonify(eventos)

    except Exception as erro:

        print(
            'Erro ao carregar calendário:',
            erro
        )

        return jsonify({
            'erro':
                'Não foi possível carregar o calendário.'
        }), 500

    finally:

        cursor.close()
        conexao.close()


# =====================================================
# FILTROS
# =====================================================

@app.route('/calendario/filtros')
def filtrosCalendario():

    conexao = criarConexao()
    cursor = conexao.cursor()

    try:

        # -------------------------------------------------
        # MODALIDADES
        # -------------------------------------------------

        cursor.execute("""
            SELECT DISTINCT fk_esporte
            FROM partidas

            WHERE fk_esporte IS NOT NULL
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL

            ORDER BY fk_esporte
        """)

        esportes = [
            linha[0]
            for linha in cursor.fetchall()
        ]


        # -------------------------------------------------
        # GÊNEROS
        # -------------------------------------------------

        cursor.execute("""
            SELECT DISTINCT fk_genero
            FROM partidas

            WHERE fk_genero IS NOT NULL
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL

            ORDER BY fk_genero
        """)

        generos = [
            linha[0]
            for linha in cursor.fetchall()
        ]


        # -------------------------------------------------
        # TURMAS
        # -------------------------------------------------

        cursor.execute("""
            SELECT pk_nome_turma
            FROM turmas
            ORDER BY pk_nome_turma
        """)

        turmas = [
            linha[0]
            for linha in cursor.fetchall()
        ]


        return jsonify({
            'esportes': esportes,
            'generos': generos,
            'turmas': turmas
        })

    except Exception as erro:

        print(
            'Erro ao carregar filtros:',
            erro
        )

        return jsonify({
            'esportes': [],
            'generos': [],
            'turmas': []
        }), 500

    finally:

        cursor.close()
        conexao.close()


# =====================================================
# PARTIDAS DISPONÍVEIS PARA ADICIONAR
# =====================================================

@app.route('/calendario/partidas')
def partidasCalendario():

    esporte = request.args.get('esporte')
    genero = request.args.get('genero')
    etapa = request.args.get(
        'etapa',
        type=int
    )

    if not esporte or not genero or etapa is None:
        return jsonify([])

    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT

                p.pk_partida,
                p.fk_esporte,
                p.fk_genero,
                p.etapa,

                ec.fk_nome_turma AS turma_casa,
                ev.fk_nome_turma AS turma_visitante

            FROM partidas p

            INNER JOIN equipes ec
                ON p.fk_equipe_casa = ec.pk_equipe

            INNER JOIN equipes ev
                ON p.fk_equipe_visitante = ev.pk_equipe

            LEFT JOIN calendario c
                ON c.fk_partida = p.pk_partida

            WHERE p.fk_esporte = %s
              AND p.fk_genero = %s
              AND p.etapa = %s
              AND c.fk_partida IS NULL

            ORDER BY p.pk_partida
        """, (
            esporte,
            genero,
            etapa
        ))

        partidas = []

        for p in cursor.fetchall():

            partidas.append({

                'pk_partida':
                    p['pk_partida'],

                'fk_esporte':
                    p['fk_esporte'],

                'fk_genero':
                    p['fk_genero'],

                'etapa':
                    p['etapa'],

                # Mantido para compatibilidade com o JS
                'equipe_casa':
                    p['turma_casa']
                    or 'Turma não informada',

                'equipe_visitante':
                    p['turma_visitante']
                    or 'Turma não informada',

                'turma_casa':
                    p['turma_casa'],

                'turma_visitante':
                    p['turma_visitante']
            })

        return jsonify(partidas)

    except Exception as erro:

        print(
            'Erro ao buscar partidas do calendário:',
            erro
        )

        return jsonify([]), 500

    finally:

        cursor.close()
        conexao.close()


# =====================================================
# ADICIONAR PARTIDA
# =====================================================

@app.route(
    '/calendario/adicionar',
    methods=['POST']
)
def adicionarCalendario():

    if session.get('nivel') not in [
        'Administrador',
        'AlunoMonitor'
    ]:

        return jsonify({
            'mensagem':
                'Apenas o Administrador ou Aluno Monitor pode alterar o calendário.'
        }), 403


    dados = request.get_json(
        silent=True
    ) or {}


    data_evento = dados.get('data')
    partida = dados.get('fk_partida')
    inicio = dados.get('hora_inicio')
    fim = dados.get('hora_fim')


    if not all([
        data_evento,
        partida,
        inicio,
        fim
    ]):

        return jsonify({
            'mensagem':
                'Preencha todos os campos.'
        }), 400


    if fim <= inicio:

        return jsonify({
            'mensagem':
                'O horário final deve ser maior que o inicial.'
        }), 400


    conexao = criarConexao()
    cursor = conexao.cursor()

    try:

        # Verifica se a partida existe
        # e possui as duas equipes.
        cursor.execute("""
            SELECT pk_partida

            FROM partidas

            WHERE pk_partida = %s
              AND fk_equipe_casa IS NOT NULL
              AND fk_equipe_visitante IS NOT NULL
        """, (partida,))


        if not cursor.fetchone():

            return jsonify({
                'mensagem':
                    'Partida inválida.'
            }), 400


        # Não permite cadastrar a mesma
        # partida duas vezes.
        cursor.execute("""
            SELECT pk_evento

            FROM calendario

            WHERE fk_partida = %s
        """, (partida,))


        if cursor.fetchone():

            return jsonify({
                'mensagem':
                    'Essa partida já está no calendário.'
            }), 400


        cursor.execute("""
            INSERT INTO calendario (
                dia_evento,
                fk_partida,
                hora_inicio,
                hora_fim
            )

            VALUES (%s, %s, %s, %s)
        """, (
            data_evento,
            partida,
            inicio,
            fim
        ))


        conexao.commit()


        return jsonify({
            'mensagem':
                'Partida adicionada!'
        })


    except Exception as erro:

        conexao.rollback()

        print(
            'Erro ao adicionar partida:',
            erro
        )

        return jsonify({
            'mensagem':
                'Erro ao adicionar partida.'
        }), 500

    finally:

        cursor.close()
        conexao.close()


# =====================================================
# EDITAR PARTIDA
# =====================================================

@app.route(
    '/calendario/editar',
    methods=['POST']
)
def editarCalendario():

    if session.get('nivel') not in [
        'Administrador',
        'AlunoMonitor'
    ]:

        return jsonify({
            'mensagem':
                'Apenas o Administrador ou Aluno Monitor pode editar.'
        }), 403


    dados = request.get_json(
        silent=True
    ) or {}


    evento = dados.get('id')
    inicio = dados.get('hora_inicio')
    fim = dados.get('hora_fim')


    if not all([
        evento,
        inicio,
        fim
    ]):

        return jsonify({
            'mensagem':
                'Dados incompletos.'
        }), 400


    if fim <= inicio:

        return jsonify({
            'mensagem':
                'O horário final deve ser maior que o inicial.'
        }), 400


    conexao = criarConexao()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            UPDATE calendario

            SET
                hora_inicio = %s,
                hora_fim = %s

            WHERE pk_evento = %s
        """, (
            inicio,
            fim,
            evento
        ))


        if cursor.rowcount == 0:

            conexao.rollback()

            return jsonify({
                'mensagem':
                    'Evento não encontrado no calendário.'
            }), 404


        conexao.commit()


        return jsonify({
            'mensagem':
                'Horário atualizado!'
        })


    except Exception as erro:

        conexao.rollback()

        print(
            'Erro ao editar:',
            erro
        )

        return jsonify({
            'mensagem':
                'Erro ao editar horário.'
        }), 500

    finally:

        cursor.close()
        conexao.close()


# =====================================================
# REMOVER PARTIDA
# =====================================================

@app.route(
    '/calendario/remover',
    methods=['POST']
)
def removerCalendario():

    if session.get('nivel') not in [
        'Administrador',
        'AlunoMonitor'
    ]:

        return jsonify({
            'mensagem':
                'Apenas o Administrador ou Aluno Monitor pode remover.'
        }), 403


    dados = request.get_json(
        silent=True
    ) or {}


    evento = dados.get('id')


    if not evento:

        return jsonify({
            'mensagem':
                'Evento inválido.'
        }), 400


    conexao = criarConexao()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            DELETE FROM calendario

            WHERE pk_evento = %s
        """, (evento,))


        if cursor.rowcount == 0:

            conexao.rollback()

            return jsonify({
                'mensagem':
                    'Evento não encontrado no calendário.'
            }), 404


        conexao.commit()


        return jsonify({
            'mensagem':
                'Partida removida do calendário!'
        })


    except Exception as erro:

        conexao.rollback()

        print(
            'Erro ao remover:',
            erro
        )

        return jsonify({
            'mensagem':
                'Erro ao remover partida.'
        }), 500

    finally:

        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(debug=True)