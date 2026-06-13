function registrarDados(cod_partida, cod_equipe_casa, cod_equipe_vistante, esporte ,genero){
    let pontos_equipe_casa = document.getElementById('pontos_equipe_casa').value
    let pontos_equipe_visitante = document.getElementById('pontos_equipe_vistante').value
    let vencedor_id = 0

    console.log(cod_equipe_casa)
    console.log(cod_equipe_vistante)
    if(pontos_equipe_casa > pontos_equipe_visitante){
        vencedor = cod_equipe_casa
    }else{
        vencedor = cod_equipe_vistante
    }

    const formData = new FormData();
    formData.append("partida_id", cod_partida);
    formData.append("vencedor_id", vencedor_id);
    formData.append("pontos_equipe_casa", pontos_equipe_casa);
    formData.append("pontos_equipe_visitante", pontos_equipe_visitante);
    formData.append("esporte", esporte);
    formData.append("genero", genero);

    fetch('/chaveamento/vencedor', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    });
}


// ----- jogadores modal -----
const modalJogadores = document.getElementById("modalJogadores");
const closeJogadores = document.getElementById("closeJogadores");
const listaJogadores = document.getElementById("listaJogadores");
const tituloEquipe = document.getElementById("tituloEquipe");
let subTituloEquipe = document.getElementById("subTituloEquipe");

// Fechar modal ao clicar no "x"
closeJogadores.onclick = () => modalJogadores.style.display = "none";

// Fechar modal ao clicar fora
window.addEventListener('click', (event) => {
    if (event.target == modalJogadores) {
        modalJogadores.style.display = "none";
    }
});

function abrirModalJogadores(idEquipe, esporte, grupo, nomeEquipe) {
    fetch(`/jogadoresPorEquipe/${idEquipe}`)
        .then(response => response.json())
        .then(data => {
            listaJogadores.innerHTML = '';
            if (data.jogadores.length === 0) {
                listaJogadores.innerHTML = '<li>Nenhum jogador nesta equipe.</li>';
            } else {
                data.jogadores.forEach(jogador => {
                    const li = document.createElement('li');
                    const check = document.createElement('input');
                    check.type = 'checkbox'
                    li.textContent = `${jogador.nome}`;
                    li.appendChild(check)
                    listaJogadores.appendChild(li);
                });
            }
            tituloEquipe.innerText = `${esporte} - ${grupo}`;
            if(subTituloEquipe) subTituloEquipe.innerText = nomeEquipe ? nomeEquipe : '';
            modalJogadores.style.display = "block";
        });
}
