let correndo = false;
let hora = 0;
let minutos = 0;
let segundos = 0;
let decimais = 0;
const botao = document.getElementById("botao");
const botao2 = document.getElementById("botao2");
const botao3 = document.getElementById("botao3");
const botao4 = document.getElementById("botao4");
const play = document.getElementById("play")
const stop = document.getElementById("stop")
const wait = document.getElementById("wait")




botao2.addEventListener("click", () => {

    correndo = false;
    clearInterval(intervalo);
    botao.classList.remove("disable");
    botao2.classList.add("disable");
    wait.style.display = "block"
    play.style.display = "none"
    stop.style.display = "none"
    
});



botao3.addEventListener("click", () => {

    correndo = false;
    clearInterval(intervalo);
    hora = 0;
    minutos = 0;
    segundos = 0;
    decimais = 0;
    mostraHora(hora);
    mostraMinutos(minutos);
    mostraSegundos(segundos);
    mostradecimais(decimais);
    wait.style.display = "none"
    play.style.display = "none"
    stop.style.display = "block"

});


botao.addEventListener("click", () => {

  if (!correndo) {
    correndo = true;
    intervalo = setInterval(() => {
    mostratempo();
    }, 10);
    play.style.display = "block"
    wait.style.display = "none"
    stop.style.display = "none"
  }
});

botao4.addEventListener("click", () => {

  correndo = false;
  clearInterval(intervalo);
  hora = 0;
  minutos = 0;
  segundos = 0;
  decimais = 0;
  mostraHora(hora);
  mostraMinutos(minutos);
  mostraSegundos(segundos);
  mostradecimais(decimais);
  if (!correndo) {
    correndo = true;
    intervalo = setInterval(() => {
    mostratempo();
    }, 10);
    play.style.display = "block"
    wait.style.display = "none"
    stop.style.display = "none"
  }




});

function mostraHora(hora) {
    
  document.getElementById("hora").innerHTML =
    hora > 9 ? hora + ":" : "0" + hora + ":";
}
function mostraMinutos(minutos) {
  document.getElementById("minutos").innerHTML =
    minutos > 9 ? minutos + ":" : "0" + minutos + ":";
}
function mostraSegundos(segundos) {
  document.getElementById("segundos").innerHTML =
    segundos > 9 ? segundos + ":" : "0" + segundos + ":";
}
function mostradecimais(decimais) {
  document.getElementById("decimais").innerHTML =
    decimais > 9 ? decimais : "0" + decimais;
}

function mostratempo() {
 
  decimais++;
  if (decimais == 100) {
    decimais = 0;
    segundos++;
    if (segundos == 60) {
      segundos = 0;
      minutos++;
      if (minutos == 60) {
        minutos = 0;
        hora++;
        mostraHora(hora);
      }
      mostraMinutos(minutos);
    }
    mostraSegundos(segundos);
  }
  mostradecimais(decimais);
}