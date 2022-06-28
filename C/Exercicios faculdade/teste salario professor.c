#include<stdio.h>
#include<locale.h>

int main () {
    setlocale(LC_ALL, "portuguese");

    float vh, ad, inss, sb;

    printf("Insira o valor da hora por aula: ");
    scanf("%f", &vh);

    printf("Insira o numero de aulas dadas: ");
    scanf("%f", &ad);

    printf("Insira a porcentagem do INSS: ");
    scanf("%f", &inss);
    inss = inss/100;
    sb = (vh*ad)*inss;

    printf("Salário bruto é: %.2f R$", sb);

}