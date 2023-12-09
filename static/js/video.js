
  
function seekToTime(seconds, jogadoresEnv, jogadoresDef) {
    var video = document.getElementById('myVideo');
    video.currentTime = seconds;

    // Atualiza a lista de jogadores atacando
    var listaAtacando = document.getElementById('jogadores-atacando-list');
    listaAtacando.innerHTML = ''; // Limpa a lista atual
    jogadoresEnv.split(',').forEach(function(jogador) {
        var li = document.createElement('li');
        li.textContent = jogador.trim();
        listaAtacando.appendChild(li);
    });

    // Atualiza a lista de jogadores defendendo
    var listaDefendendo = document.getElementById('jogadores-defendendo-list');
    listaDefendendo.innerHTML = ''; // Limpa a lista atual
    jogadoresDef.split(',').forEach(function(jogador) {
        var li = document.createElement('li');
        li.textContent = jogador.trim();
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

function filterCruzamentos() {
    var desfechoFilter = document.getElementById('desfecho').value;
    var zonaFilter = document.getElementById('zona').value;

    var cruzamentos = document.getElementsByClassName('cruzamento');

    for (var i = 0; i < cruzamentos.length; i++) {
        var cruzamento = cruzamentos[i];

        var desfechoMatch = cruzamento.dataset.desfecho;
        var zonaMatch = cruzamento.dataset.zona;

        if ((desfechoMatch === desfechoFilter || desfechoFilter === 'all') && (zonaMatch === zonaFilter || zonaFilter === 'all')) {
            cruzamento.style.display = '';
        } else {
            cruzamento.style.display = 'none';
        }
    }
}

function filterTimeCruzamento() {
    var timeFilter = document.getElementById('time').value;

    var palmeiras = document.getElementById('Filtro-Palmeiras');
    var bragantino = document.getElementById('Filtro-Bragantino');

    if (timeFilter === 'Palmeiras') {
        palmeiras.style.display = '';
        bragantino.style.display = 'none';
    } else if (timeFilter === 'Bragantino') {
        palmeiras.style.display = 'none';
        bragantino.style.display = '';
    } else {
        palmeiras.style.display = '';
        bragantino.style.display = '';
    }
}