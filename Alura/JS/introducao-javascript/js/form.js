var botao = document.querySelector("#adicionar-paciente");

botao.addEventListener("click", function (event){
    event.preventDefault();
    
    var form = document.querySelector("#form-adiciona");
    var paciente = catpaciente(form);

    var pacientetr = document.createElement("tr");
    var pesotd = document.createElement("td");
    var nometd = document.createElement("td");
    var alturatd = document.createElement("td");
    var gorduratd = document.createElement("td");
    var imctd = document.createElement("td");

    var listatd = [nometd, pesotd, alturatd, gorduratd, imctd];
    pesotd.textContent = paciente.peso;
    nometd.textContent = paciente.nome;
    alturatd.textContent = paciente.altura;
    gorduratd.textContent = paciente.gordura;
    imctd.textContent = calculaImc(paciente.peso, paciente.altura);

    for(i = 0; i < listatd.length; i++){
        pacientetr.appendChild(listatd[i]);
    }

    var tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(pacientetr);
    
});


function catpaciente(form){
    var paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value
    }
    return paciente;
}