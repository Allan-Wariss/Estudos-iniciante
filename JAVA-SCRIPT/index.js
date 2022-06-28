import { Cliente } from "./Cliente.js"
import { ContaCorrente } from "./ContaCorrente.js"


const cliente1 = new Cliente("Allan", 66600022299910);
const ContaCorrenteAllan = new ContaCorrente();


ContaCorrenteAllan.depositar(100);



const cliente2 = new Cliente("Leticia", 22200033399912);
const ContaCorrenteLeticia = new ContaCorrente(1001,cliente2.nome);

ContaCorrenteAllan.transferir(50,ContaCorrenteLeticia);

console.log(cliente1,ContaCorrenteAllan, ContaCorrente.numeroDeContas);