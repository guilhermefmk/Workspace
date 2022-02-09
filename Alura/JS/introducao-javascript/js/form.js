var botao = document.querySelector("#adicionar-paciente");

botao.addEventListener("click", function (event){
    event.preventDefault();
    
    var form = document.querySelector("#form-adiciona");
    var paciente = catpaciente(form);

    var pacientetr = montaTr(paciente);

    var tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(pacientetr);
    
    form.reset();
});


function catpaciente(form){
    var paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaImc(form.peso.value, form.altura.value)
    }
    return paciente;
}

function montaTr(paciente){

    var pacientetr = document.createElement("tr");
    pacientetr.classList.add("paciente");

    var pesotd = montaTd(paciente.peso, "info-peso");
    var nometd = montaTd(paciente.nome, "info-nome");
    var alturatd = montaTd(paciente.altura, "info-altura");
    var gorduratd = montaTd(paciente.gordura, "info-gordura");
    var imctd = montaTd(paciente.imc, "info-imc");

    var listatd = [nometd, pesotd, alturatd, gorduratd, imctd];

    for(i = 0; i < listatd.length; i++){
        pacientetr.appendChild(listatd[i]);
    }

    return pacientetr;
}

function montaTd(dado, classe){
    var td = document.createElement("td");
    td.textContent = dado;
    td.classList.add(classe);

    return td;
}