document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // MODAL DE CADASTRO
    // =====================================================

    const modalNova =
        document.getElementById("modalNovaModalidade");

    const btnNova =
        document.getElementById("btnNovaModalidade");

    const btnFecharNova =
        document.getElementById("btnFecharNovaModal");

    const btnCancelarNova =
        document.getElementById("btnCancelarNovaModalidade");

    const formNova =
        document.getElementById("formNovaModalidade");

    const mensagemNova =
        document.getElementById("mensagemNovaModalidade");


    // =====================================================
    // MODAL DE EDIÇÃO
    // =====================================================

    const modalEditar =
        document.getElementById("modalEditarModalidade");

    const btnFecharEditar =
        document.getElementById("btnFecharEditarModal");

    const btnCancelarEditar =
        document.getElementById("btnCancelarEdicao");

    const formEditar =
        document.getElementById("formEditarModalidade");

    const mensagemEditar =
        document.getElementById("mensagemEditarModalidade");


    // =====================================================
    // FUNÇÃO DE LIMPAR MENSAGEM
    // =====================================================

    function limparMensagem(elemento) {

        elemento.textContent = "";
        elemento.style.display = "none";

    }


    // =====================================================
    // ABRIR MODAL DE CADASTRO
    // =====================================================

    function abrirModalNova() {

        modalNova.style.display = "flex";

        document
            .getElementById("nome_modalidade")
            .focus();

    }


    // =====================================================
    // FECHAR MODAL DE CADASTRO
    // =====================================================

    function fecharModalNova() {

        modalNova.style.display = "none";

        formNova.reset();

        document.getElementById("ativo").value = "1";

        limparMensagem(mensagemNova);

    }


    // =====================================================
    // ABRIR MODAL DE EDIÇÃO
    // =====================================================

    function abrirModalEditar(botao) {

        const id = botao.dataset.id || "";
        const nome = botao.dataset.nome || "";
        const descricao = botao.dataset.descricao || "";
        const ativo = botao.dataset.ativo || "1";

        console.log("=================================");
        console.log("EDITANDO MODALIDADE");
        console.log("ID:", id);
        console.log("Nome:", nome);
        console.log("Descrição:", descricao);
        console.log("Ativo:", ativo);
        console.log("Elemento:", botao);
        console.log("=================================");


        // Preenche o ID
        document.getElementById(
            "editar_pk_modalidade"
        ).value = id;


        // Preenche o nome
        document.getElementById(
            "editar_nome_modalidade"
        ).value = nome;


        // Preenche a descrição
        document.getElementById(
            "editar_descricao"
        ).value = descricao;


        // Preenche o status
        document.getElementById(
            "editar_ativo"
        ).value = ativo;


        // Limpa mensagem anterior
        limparMensagem(mensagemEditar);


        // Abre o modal
        modalEditar.style.display = "flex";


        // Coloca cursor no nome
        document.getElementById(
            "editar_nome_modalidade"
        ).focus();
    }

    // =====================================================
    // FECHAR MODAL DE EDIÇÃO
    // =====================================================

    function fecharModalEditar() {

        modalEditar.style.display = "none";

        formEditar.reset();

        limparMensagem(mensagemEditar);

    }


    // =====================================================
    // BOTÃO "NOVA MODALIDADE"
    // =====================================================

    btnNova.addEventListener(
        "click",
        abrirModalNova
    );


    // =====================================================
    // BOTÃO X - CADASTRO
    // =====================================================

    btnFecharNova.addEventListener(
        "click",
        fecharModalNova
    );


    // =====================================================
    // BOTÃO CANCELAR - CADASTRO
    // =====================================================

    btnCancelarNova.addEventListener(
        "click",
        fecharModalNova
    );


    // =====================================================
    // BOTÃO X - EDIÇÃO
    // =====================================================

    btnFecharEditar.addEventListener(
        "click",
        fecharModalEditar
    );


    // =====================================================
    // BOTÃO CANCELAR - EDIÇÃO
    // =====================================================

    btnCancelarEditar.addEventListener(
        "click",
        fecharModalEditar
    );


    // =====================================================
    // BOTÕES "EDITAR"
    // =====================================================

    document
        .querySelectorAll(".btn-editar-modalidade")
        .forEach(function (botao) {

            botao.addEventListener(
                "click",
                function () {

                    abrirModalEditar(this);

                }
            );

        });


    // =====================================================
    // CLICAR FORA DO MODAL
    // =====================================================

    modalNova.addEventListener(
        "click",
        function (event) {

            if (event.target === modalNova) {

                fecharModalNova();

            }

        }
    );


    modalEditar.addEventListener(
        "click",
        function (event) {

            if (event.target === modalEditar) {

                fecharModalEditar();

            }

        }
    );


    // =====================================================
    // TECLA ESC
    // =====================================================

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key !== "Escape") {
                return;
            }


            if (modalNova.style.display === "flex") {

                fecharModalNova();

                return;

            }


            if (modalEditar.style.display === "flex") {

                fecharModalEditar();

            }

        }
    );


    // =====================================================
    // CADASTRAR MODALIDADE
    // =====================================================

    formNova.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();


            const formData =
                new FormData(formNova);


            try {

                const resposta = await fetch(
                    "/tabelaAtletismo/Modalidades",
                    {
                        method: "POST",
                        body: formData
                    }
                );


                const resultado =
                    await resposta.json();


                mensagemNova.textContent =
                    resultado.mensagem;

                mensagemNova.style.display =
                    "block";


                if (resultado.status === "sucesso") {

                    setTimeout(
                        function () {

                            fecharModalNova();

                            window.location.reload();

                        },
                        800
                    );

                }

            } catch (erro) {

                console.error(
                    "Erro ao cadastrar modalidade:",
                    erro
                );


                mensagemNova.textContent =
                    "Não foi possível cadastrar a modalidade.";

                mensagemNova.style.display =
                    "block";

            }

        }
    );


    

    // =====================================================
    // EDITAR MODALIDADE
    // =====================================================

    formEditar.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();


            const formData =
                new FormData(formEditar);


            try {

                const resposta = await fetch(
                    "/tabelaAtletismo/Modalidades",
                    {
                        method: "POST",
                        body: formData
                    }
                );


                const resultado =
                    await resposta.json();


                mensagemEditar.textContent =
                    resultado.mensagem;

                mensagemEditar.style.display =
                    "block";


                if (resultado.status === "sucesso") {

                    setTimeout(
                        function () {

                            fecharModalEditar();

                            window.location.reload();

                        },
                        800
                    );

                }

            } catch (erro) {

                console.error(
                    "Erro ao editar modalidade:",
                    erro
                );


                mensagemEditar.textContent =
                    "Não foi possível editar a modalidade.";

                mensagemEditar.style.display =
                    "block";

            }

        }
    );

});

// =====================================================
// BOTÕES "EXCLUIR"
// =====================================================

document
    .querySelectorAll(".btn-delete")
    .forEach(function (botao) {

        botao.addEventListener(
            "click",
            async function () {

                const id = this.dataset.id;

                if (!id) {

                    console.error(
                        "ID da modalidade não encontrado."
                    );

                    alert(
                        "Não foi possível identificar a modalidade."
                    );

                    return;
                }


                try {

                    const resposta = await fetch(
                        "/tabelaAtletismo/Modalidades",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type": "application/json"
                            },

                            body: JSON.stringify({
                                acao: "deletar",
                                pk_modalidade: id
                            })
                        }
                    );


                    const resultado =
                        await resposta.json();


                    if (resultado.status === "sucesso") {

                        window.location.reload();

                    } else {

                        alert(
                            resultado.mensagem
                        );

                    }

                } catch (erro) {

                    console.error(
                        "Erro ao excluir modalidade:",
                        erro
                    );

                    alert(
                        "Não foi possível excluir a modalidade."
                    );

                }

            }
        );

    });