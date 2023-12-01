
  

function seekToTime(seconds, cruzamentoIndex) {
    var video = document.getElementById("myVideo");
    var newTime = seconds - 5; // Subtrai 5 segundos do tempo de cruzamento

    video.currentTime = newTime >= 0 ? newTime : 0; // Evita definir um tempo negativo

    var cruzamento = cruzamentos[cruzamentoIndex - 1]; // Ajuste conforme a estrutura de dados

    // Atualizar lista de jogadores atacando
    var listaAtacando = document.getElementById("jogadores-atacando-list");
    listaAtacando.innerHTML = ''; // Limpar lista atual
    cruzamento.nome_jogadores_time_cruzando.forEach(function(jogador) {
        var li = document.createElement("li");
        li.textContent = jogador;
        listaAtacando.appendChild(li);
    });

    // Atualizar lista de jogadores defendendo
    var listaDefendendo = document.getElementById("jogadores-defendendo-list");
    listaDefendendo.innerHTML = ''; // Limpar lista atual
    cruzamento.nome_jogadores_time_defendendo.forEach(function(jogador) {
        var li = document.createElement("li");
        li.textContent = jogador;
        listaDefendendo.appendChild(li);
    });
}



function showPercentage(element) {
    // Salva o nome original da zona se ainda não foi salvo
    if (!element.dataset.originalName) {
        element.dataset.originalName = element.querySelector('.info').textContent;
    }
    // Define a porcentagem (isso deve ser ajustado para cada zona, se for diferente)
    element.querySelector('.info').textContent = element.dataset.percentage || '25%';
}

function showName(element) {
    // Retorna ao nome original da zona
    element.querySelector('.info').textContent = element.dataset.originalName;
}

function retroceder(segundos) {
    var video = document.getElementById("myVideo");
    video.currentTime -= segundos;
}

function avançar(segundos) {
    var video = document.getElementById("myVideo");
    video.currentTime += segundos;
}

function playPause() {
    var video = document.getElementById("myVideo");
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
}
