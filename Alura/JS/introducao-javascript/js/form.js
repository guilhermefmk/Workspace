var botao = document.querySelector("#adicionar-paciente");

botao.addEventListener("click", function (event){
    event.preventDefault();
    
    var form = document.querySelector("#form-adiciona");
    var altura = form.altura.value;
    var peso = form.peso.value;
    var nome = form.nome.value;
    var gordura  = form.gordura.value;

    var pacientetr = document.createElement("tr");
    var pesotd = document.createElement("td");
    var nometd = document.createElement("td");
    var alturatd = document.createElement("td");
    var gorduratd = document.createElement("td");
    var imctd = document.createElement("td");

    var listatd = [nometd, pesotd, alturatd, gorduratd, imctd];
    pesotd.textContent = peso;
    nometd.textContent = nome;
    alturatd.textContent = altura;
    gorduratd.textContent = gordura;
    imctd.textContent = imc.toFixed(2);

    for(i = 0; i < listatd.length; i++){
        pacientetr.appendChild(listatd[i]);
    }

    var tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(pacientetr);
    
});