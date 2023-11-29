function setVideoTime() {
    var video = document.getElementById("myVideo");
    var minute = document.getElementById("minuteInput").value;
    video.currentTime = minute * 60; // Converte minutos em segundos
  }
  