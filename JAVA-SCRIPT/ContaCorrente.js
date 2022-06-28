export class ContaCorrente{
    _agencia;
    _cliente;
    static numeroDeContas=0;
    
    _saldo;

    get cliente(){
        return this._cliente;
    }
    get agencia(){
        return this.agencia;
    }


    constructor(agencia, cliente){
        this._agencia = agencia;
        this._cliente = cliente;
        ContaCorrente.numeroDeContas +=1;
    }

    sacar(valor){
        if(this._saldo >= valor){
            this._saldo -= valor;
            return valor;
        }
    }

    depositar(valor){
        if(valor >=0){
            this._saldo += valor;
            return valor;
        }
    }
    transferir(valor, conta){
        const valorSacado = this.sacar(valor);
        conta.depositar(valorSacado);

    }
}