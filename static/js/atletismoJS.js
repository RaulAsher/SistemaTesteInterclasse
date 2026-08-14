document.addEventListener("DOMContentLoaded", function () {

    const modal = document.getElementById("modalNovaProva");

    const btnAbrir =
        document.getElementById("btnAbrirModalProva");

    const btnFechar =
        document.getElementById("btnFecharModalProva");


    // ABRIR MODAL
    btnAbrir.addEventListener("click", function () {

        modal.style.display = "block";

    });


    // FECHAR NO X
    btnFechar.addEventListener("click", function () {

        modal.style.display = "none";

    });


    // FECHAR CLICANDO NO FUNDO ESCURO
    window.addEventListener("click", function (event) {

        if (event.target === modal) {

            modal.style.display = "none";

        }

    });


    // FECHAR COM ESC
    document.addEventListener("keydown", function (event) {

        if (
            event.key === "Escape" &&
            modal.style.display === "block"
        ) {

            modal.style.display = "none";

        }

    });

});