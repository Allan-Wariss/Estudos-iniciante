var titulo = document.querySelector(".titulo");
titulo.textContent= "Sumida Nutricionista";//teste para trocar titulo

var pacientes = document.querySelectorAll(".paciente");


for(var i = 0 ; i < pacientes.length; i++){

    var paciente = pacientes[i]

    var tdPeso = paciente.querySelector(".info-peso");
    var peso = tdPeso.textContent;

    var tdAltura = paciente.querySelector(".info-altura")
    var altura = tdAltura.textContent;


    var tdImc = paciente.querySelector(".info-imc");

    var pesoEhValidio = true;
    var alturaEhValida = true;
    
    if(peso<=0 || peso>=300){
        console.log("Peso Inválido");
        pesoEhValidio = false;
        tdImc.textContent = "Peso Inválido";
        paciente.classList.add("paciente-ivalido");
    }

    if(altura<=0 || altura>=2.4){
        console.log("Altura Inválido");
        alturaEhValida = false;
        tdImc.textContent = "Altura Inválido";
        paciente.classList.add("paciente-ivalido");
    }
    if (pesoEhValidio && alturaEhValida){
        var imc = calculaImc(peso,altura)
        tdImc.textContent = imc;
    }
}

function calculaImc(peso,altura){
    var imc = 0;

    imc = peso/(altura * altura);

    return imc.toFixed(2);
}
