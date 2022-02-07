var pacientes = document.querySelectorAll(".paciente");
var botao = document.querySelector("#adicionar-paciente");


for(i = 0; i < pacientes.length; i++){
    var paciente = pacientes[i];
    var tdPeso = paciente.querySelector(".info-peso");
    var tdAltura = paciente.querySelector(".info-altura");
    var tdImc = paciente.querySelector(".info-imc");
    var altura = tdAltura.textContent;
    var peso = tdPeso.textContent;
    var alturaEhValida = true;
    var pesoEhValido = true;
    

    if (altura < 0 || altura > 3.00){
        tdAltura.textContent = "Altura inválida";
        alturaEhValida = false;
        tdAltura.classList.add("erro");
    }
    if (altura < 0 || peso > 300){
        tdAltura.textContent = "Peso inválido";
        pesoEhValido = false;
        tdAltura.classList.add("erro");
    }
    if (pesoEhValido == true && alturaEhValida == true){
        var imc = peso / (altura * altura);
        tdImc.textContent = imc.toFixed(2);
    }
    else {
        tdImc.classList.add("erro");
        tdImc.textContent = "Erro";
    }
}

botao.addEventListener("click", function (event){
    event.preventDefault();
    console.log("Clique");
});
