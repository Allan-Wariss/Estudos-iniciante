var botaoAdicionar = document.querySelector("#adicionar-paciente");
botaoAdicionar.addEventListener("click", function(event) {
    event.preventDefault();

    console.log("Oi eu sou o botao e fui clicado");
    
    var form = document.querySelector("#form-adiciona");
    var nome = form.nome.value;
    var peso = form.peso.value;
    var altura = parseFloat(form.altura.value.replace(/,/, '.'));//NOTA IMPORTANTE! O JS só faz calculo decimal com "." e não ","; Se a "," for usada o resultado é NaN
    //Este comando "parseFloat(form.altura.value.replace(/,/, '.'))" faz com que a virgula seja trocada pelo "." no calculo caso o usuario digite com o padrão brasileiro decimal.
    var gordura = form.gordura.value;

    var pacienteTr = document.createElement("tr");

    var nomeTd = document.createElement("td");
    var pesoTd = document.createElement("td");
    var alturaTd = document.createElement("td");
    var gorduraTd = document.createElement("td");
    tdImc = document.createElement("td");

    nomeTd.textContent = nome;
    pesoTd.textContent = peso;
    alturaTd.textContent = altura;
    gorduraTd.textContent = gordura;
    tdImc.textContent = calculaImc(peso,altura);

    if(form.nome.value == false,form.peso.value == false,form.altura.value == false,form.gordura.value == false){
        window.alert("Não deixe nenhum campo vazio!");
        return form;
    }

    pacienteTr.appendChild(nomeTd);
    pacienteTr.appendChild(pesoTd);
    pacienteTr.appendChild(alturaTd);
    pacienteTr.appendChild(gorduraTd);
    pacienteTr.appendChild(tdImc);

    var tabela = document.querySelector("#tabela-pacientes");

    tabela.appendChild(pacienteTr);
    
});

console.log(calculaImc)