document.addEventListener("DOMContentLoaded", function () {

    function normalizar(texto) {
        return String(texto || "")
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");
    }

    function primeiroValor(form, ids = [], names = []) {
        for (const id of ids) {
            const elemento = document.getElementById(id);
            if (elemento && elemento.value) return elemento.value.trim();
        }

        for (const name of names) {
            const elemento = form.querySelector(`[name="${name}"]`);
            if (elemento && elemento.value) return elemento.value.trim();
        }

        return "";
    }

    function obterAcao(form, botao) {
        const action = normalizar(form.getAttribute("action"));
        const textoBotao = normalizar(
            botao?.value || botao?.textContent || ""
        );

        if (
            action.includes("deletar") ||
            action.includes("remover") ||
            action.includes("excluir") ||
            textoBotao.includes("deletar") ||
            textoBotao.includes("remover") ||
            textoBotao.includes("excluir")
        ) {
            return "excluir";
        }

        if (
            action.includes("editar") ||
            action.includes("alterar") ||
            action.includes("atualizar") ||
            textoBotao.includes("editar") ||
            textoBotao.includes("alterar") ||
            textoBotao.includes("atualizar") ||
            textoBotao.includes("salvar alteracoes")
        ) {
            return "alterar";
        }

        if (
            action.includes("cadastrar") ||
            action.includes("criar") ||
            action.includes("inscrever") ||
            textoBotao.includes("cadastrar") ||
            textoBotao.includes("criar") ||
            textoBotao.includes("inscrever")
        ) {
            return "cadastrar";
        }

        return null;
    }

    function possuiConfirmacaoPropria(form) {
        if (form.dataset.semConfirmacao === "true") return true;
        if (form.dataset.confirmacaoPropria === "true") return true;

        if (form.getAttribute("onsubmit")) {
            const onsubmit = normalizar(form.getAttribute("onsubmit"));
            if (onsubmit.includes("confirm(")) return true;
        }

        const elementoComConfirmacao = form.querySelector(
            '[onclick*="confirm"], [onclick*="confirmar"]'
        );

        return !!elementoComConfirmacao;
    }

    function montarMensagem(form, botao, acao) {
        const action = normalizar(form.getAttribute("action"));

        const nome = primeiroValor(
            form,
            [
                "editNome",
                "editUsuario",
                "editTurma",
                "nome",
                "pk_usuario",
                "pk_nome_turma"
            ],
            ["nome", "pk_usuario", "pk_nome_turma"]
        );

        const matricula = primeiroValor(
            form,
            ["editMatricula", "matricula", "nova_matricula"],
            ["matricula", "nova_matricula"]
        );

        const equipe = primeiroValor(
            form,
            ["editId", "pk_equipe"],
            ["pk_equipe"]
        );

        const modalidade = primeiroValor(
            form,
            ["editEsporte", "fk_esporte", "esporte"],
            ["fk_esporte", "esporte"]
        );

        if (acao === "excluir") {
            if (action.includes("aluno")) {
                return nome
                    ? `Deseja realmente excluir o aluno "${nome}"?\n\nEsta ação não poderá ser desfeita.`
                    : "Deseja realmente excluir este aluno?\n\nEsta ação não poderá ser desfeita.";
            }

            if (action.includes("turma")) {
                return nome
                    ? `Deseja realmente excluir a turma "${nome}"?\n\nEsta ação não poderá ser desfeita.`
                    : "Deseja realmente excluir esta turma?\n\nEsta ação não poderá ser desfeita.";
            }

            if (action.includes("equipe")) {
                return equipe
                    ? `Deseja realmente excluir a equipe ${equipe}?\n\nEsta ação não poderá ser desfeita.`
                    : "Deseja realmente excluir esta equipe?\n\nEsta ação não poderá ser desfeita.";
            }

            if (action.includes("usuario")) {
                return nome
                    ? `Deseja realmente excluir o usuário "${nome}"?\n\nO acesso ao sistema será removido.`
                    : "Deseja realmente excluir este usuário?\n\nO acesso ao sistema será removido.";
            }

            return "Deseja realmente excluir este registro?\n\nEsta ação não poderá ser desfeita.";
        }

        if (acao === "alterar") {
            if (action.includes("aluno")) {
                const detalhes = matricula ? `\nMatrícula: ${matricula}` : "";
                return nome
                    ? `Deseja realmente alterar os dados do aluno "${nome}"?${detalhes}`
                    : "Deseja realmente alterar os dados deste aluno?";
            }

            if (action.includes("turma")) {
                return nome
                    ? `Deseja realmente alterar a turma "${nome}"?`
                    : "Deseja realmente alterar esta turma?";
            }

            if (action.includes("equipe")) {
                const detalhes = modalidade ? `\nModalidade: ${modalidade}` : "";
                return equipe
                    ? `Deseja realmente alterar a equipe ${equipe}?${detalhes}`
                    : "Deseja realmente alterar esta equipe?";
            }

            if (action.includes("usuario")) {
                return nome
                    ? `Deseja realmente alterar o usuário "${nome}"?`
                    : "Deseja realmente alterar este usuário?";
            }

            return "Deseja realmente alterar estes dados?\n\nConfira as informações antes de continuar.";
        }

        if (acao === "cadastrar") {
            if (action.includes("aluno")) {
                return nome
                    ? `Deseja realmente cadastrar o aluno "${nome}"?`
                    : "Deseja realmente cadastrar este aluno?";
            }

            if (action.includes("equipe")) {
                return modalidade
                    ? `Deseja realmente cadastrar esta equipe na modalidade "${modalidade}"?`
                    : "Deseja realmente cadastrar esta equipe?";
            }

            if (action.includes("usuario")) {
                return nome
                    ? `Deseja realmente cadastrar o usuário "${nome}"?`
                    : "Deseja realmente cadastrar este usuário?";
            }

            if (action.includes("turma")) {
                return nome
                    ? `Deseja realmente cadastrar a turma "${nome}"?`
                    : "Deseja realmente cadastrar esta turma?";
            }

            return "Deseja realmente salvar este cadastro?";
        }

        return "Tem certeza que deseja continuar?";
    }

    document.addEventListener("submit", function (event) {
        const form = event.target;

        if (!(form instanceof HTMLFormElement)) return;
        if (possuiConfirmacaoPropria(form)) return;

        const botao = form.querySelector(
            'button[type="submit"], input[type="submit"]'
        );

        const acao = obterAcao(form, botao);
        if (!acao) return;

        if (!window.confirm(montarMensagem(form, botao, acao))) {
            event.preventDefault();
            event.stopImmediatePropagation();
        }
    }, true);

    document.addEventListener("click", function (event) {
        const link = event.target.closest("a");
        if (!link) return;

        const href = normalizar(link.getAttribute("href"));
        const texto = normalizar(link.textContent);

        const exclusao =
            href.includes("deletar") ||
            href.includes("remover") ||
            href.includes("excluir") ||
            texto.includes("deletar") ||
            texto.includes("remover") ||
            texto.includes("excluir");

        if (!exclusao) return;

        if (
            link.closest("#modalConfirmacao") ||
            link.closest(".modal-confirmacao")
        ) {
            return;
        }

        if (!window.confirm(
            "Deseja realmente excluir este registro?\n\nEsta ação não poderá ser desfeita."
        )) {
            event.preventDefault();
        }
    }, true);
});
