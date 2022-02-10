


var pacientes = document.querySelectorAll(".paciente");


for(i = 0; i < pacientes.length; i++){
    var paciente = pacientes[i];
    var tdPeso = paciente.querySelector(".info-peso");
    var tdAltura = paciente.querySelector(".info-altura");
    var tdImc = paciente.querySelector(".info-imc");
    var altura = tdAltura.textContent;
    var peso = tdPeso.textContent;

    console.log(validaPeso(peso));

    if (validaAltura(altura) == false){
        tdAltura.textContent = "Altura inválida";
        tdAltura.classList.add("erro");
    }
    if (validaPeso(peso) == false){
        tdPeso.textContent = "Peso inválido";
        tdPeso.classList.add("erro");
    }
    if (validaAltura(altura) == true && validaPeso(peso) == true){
        tdImc.textContent = calculaImc(peso, altura);
    }else{
        tdImc.classList.add("erro");
        tdImc.textContent = "Erro";
    }
}

function calculaImc(peso,altura){
    var imc = 0;

    imc = peso / (altura * altura);

    return imc.toFixed(2);
}

function validaPeso(peso){
    if(peso > 0 && peso < 300){
        return true;
    }else{
        return false;
    }
}
function validaAltura(altura){
    if(altura > 0 && altura < 3.0){
        return true;
    }else{
        return false;
    }
}


