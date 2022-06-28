var titulo = document.querySelector(".titulo");
titulo.textContent= "Sumida Nutricionista";

var paciente = document.querySelector("#primeiro-paciente");
var tdPeso = document.querySelector(".info-peso");
var peso = tdPeso.textContent;

var tdAltura = document.querySelector(".info-altura")
var altura = tdAltura.textContent;


var tdImc = document.querySelector(".info-imc");

var pesoEhValidio = true;
var alturaEhValida = true;

if(peso<=0 || peso>=600){
    console.log("Peso Inválido");
    pesoEhValidio = false;
    tdImc.textContent = "Peso Inválido";
}

if(altura<=0 || altura>=3.0){
    console.log("Altura Inválido");
    alturaEhValida = false;
    tdImc.textContent = "Altura Inválido";
}
if (pesoEhValidio && alturaEhValida){
    var imcCalculo = peso/(altura * altura);
    tdImc.textContent = imcCalculo;
}


console.log(peso);
console.log(altura);
console.log(imcCalculo);