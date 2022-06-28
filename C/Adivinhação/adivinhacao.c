#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	//Imprime
	printf("**********************************\n");
	printf("*Bem-vindo ao jogo de adivinhacao*\n");
	printf("**********************************\n");
    printf("      Escolha a dificuldade:\n");
	printf("   Facil(1) Medio(2) Dificil(3)\n");
	

	srand(time(NULL));
	int NUMERO_SECRETO = rand() % 100;
	int chute;

	int numero_de_tentativas;
	int tentativas = 0;
	double pontos = 1000;

	int dificuldade;
	scanf("%d", &dificuldade);
	switch (dificuldade)
	{
	case 1:
		numero_de_tentativas = 15;
		break;
	case 2:
		numero_de_tentativas = 10;
		break;
	case 3:
		numero_de_tentativas = 5;
	}

    printf("Voce tem %d Tentativas \n", numero_de_tentativas);

	for(tentativas = 1; tentativas <= numero_de_tentativas; tentativas++){

		printf("\n");
		printf("Tentativa: %d\n", tentativas);
		printf("Qual e o seu chute? ");
		scanf("%d", &chute);
		printf("Seu chute foi %d\n", chute);
		printf("\n");


		int acertou = chute == NUMERO_SECRETO;
		int maior = chute > NUMERO_SECRETO;
		double pontosperdidos = abs(chute - NUMERO_SECRETO) / (double) 2;
		pontos = pontos - pontosperdidos;

		if(acertou){
			printf("Parabens voce acertou!\n");
			printf("Total de pontos: %.1f\n", pontos);
			break;
		}
		else{
			if(maior){
				printf("Seu chute foi MAIOR que o numero secreto\n");
			}
			else{
				printf("Seu chute foi MENOR que o numero secreto\n");
			}
		}	
	}
	if(tentativas >= numero_de_tentativas){
		printf("Suas tentativas acabaram!\n");
		printf("Tente de novo\n");
	}
	printf("\n");
	printf("Total de pontos: %.1f\n", pontos);

}