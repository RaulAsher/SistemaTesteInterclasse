document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("menuToggle");
    const barraLateral = document.getElementById("barraLateral");

    if (!btn || !barraLateral) return;

    function abrirMenu() {
        barraLateral.classList.add("open");
        btn.setAttribute("aria-label", "Fechar menu");
    }

    function fecharMenu() {
        barraLateral.classList.remove("open");
        btn.setAttribute("aria-label", "Abrir menu");
    }

    btn.addEventListener("click", function (event) {
        event.stopPropagation();
        barraLateral.classList.contains("open") ? fecharMenu() : abrirMenu();
    });

    document.addEventListener("click", function (event) {
        if (!window.matchMedia("(max-width: 900px)").matches) return;
        if (!barraLateral.classList.contains("open")) return;

        if (!barraLateral.contains(event.target) && !btn.contains(event.target)) {
            fecharMenu();
        }
    });

    barraLateral.addEventListener("click", function (event) {
        event.stopPropagation();
    });

    const toggle = document.querySelector(".submenu-toggle");
    const submenu = document.querySelector(".submenu");

    if (toggle && submenu) {
        toggle.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();

            submenu.classList.toggle("active");
            const aberto = submenu.classList.contains("active");

            toggle.innerHTML = toggle.innerHTML
                .replace("▾", "")
                .replace("▴", "")
                .trim() + (aberto ? " ▴" : " ▾");
        });
    }
});
