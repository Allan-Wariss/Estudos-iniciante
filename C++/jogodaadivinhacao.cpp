#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main (){
    cout << "**********************************" << endl;
    cout << "*Bem-Vindo ao jogo da adivinhacao*" << endl;
    cout << "**********************************" << endl;
    cout << "      Escolha a dificuldade:" << endl;
    cout << "   Facil(F) Medio(M) Dificil(D)" << endl;

    char dificuldade;
    cin >> dificuldade;

    int numero_de_tentativas;
    if(dificuldade == 'F'|| dificuldade =='f'){
        numero_de_tentativas = 15;
    }
    else if(dificuldade == 'M'|| dificuldade == 'm'){
        numero_de_tentativas = 10;
    }
    else{
        numero_de_tentativas = 5;
    }

    srand(time(NULL));
    const int NUMERO_SECRETO = rand() % 100;
    bool nao_acertou = true;
    int tentativas = 0;
    double pontos = 1000;

    for(tentativas = 1; tentativas <= numero_de_tentativas;tentativas++){
        int chute;
        cout << "Tentativa " << tentativas << endl;
        cout << "Digite seu chute:";
        cin >> chute;
        cout << "Seu chute e: " << chute << endl;
        cout << endl;

        bool acertou = chute == NUMERO_SECRETO;
        bool maior = chute > NUMERO_SECRETO;
        double pontos_perdidos = abs(chute - NUMERO_SECRETO)/2.0;
        pontos = pontos - pontos_perdidos; 

        if(acertou){
            cout << "Parabens voce acertou!"<< endl;
            nao_acertou = false;
            break;
        }
        else if(maior){
            cout << "O seu chute foi maior que o numero secreto"<< endl;
        }
        else {
            cout << "O seu chute foi menor que o numero secreto"<< endl;
        }
    }
    cout << "Fim do jogo" << endl;
    if(nao_acertou){
        cout << "Voce perdeu, tente novamente!" << endl;
    }
    else{
        cout << "Voce acertou em " << tentativas << " tentativas!" << endl;
        cout.precision(2);
        cout << fixed;
        cout << "Voce fez " << pontos << " pontos!" << endl;
    }
}