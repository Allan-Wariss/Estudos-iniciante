// tem que ser maior de idade
// se for menor de idade tem que estar acompanhado
// se não, não compra

const lista = [`SP`, `RJ`, `BH`, `CE`];
let idade = 18;
let acompanhado = false;

if (idade >= 18 || acompanhado == true) {
    console.log("Pode viajar!");
    lista.splice(1, 1); //mt perigoso o rio
    console.log("Destinos: ", lista);
}
else {
    console.log("AAAA NÃO VAI!");
}