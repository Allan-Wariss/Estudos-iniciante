const lista = [`SP`, `RJ`, `BH`, `CE`];
let idade = 18;
let acompanhado = false;
let temPassagem = false;
const destino = `SP`;

console.log("Destinos: ");
console.log(lista);

const podeComprar = idade >= 18 || acompanhado == true;

let contador = 0;
let destinoExiste = false;

while(contador<4){
    if(lista[contador] == destino){
        destinoExiste = true;
        break
    }
    contador +=1;
}
console.log("Destino Existe: ", destinoExiste);
