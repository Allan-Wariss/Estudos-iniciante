#include <stdio.h>

int main(){
    float altura, peso;
    char sexo ;

    printf("Insira a sua altura: ");
    scanf("%f", &altura);

    printf("Insira o sexo: h ou m ");
    scanf("%s", &sexo);

    if(sexo == 'h'){
        peso = 51 * altura;
        printf("Seu peso ideal e: %.2f", peso);
    }
    else{
        peso = 60 * altura;
        printf("Seu peso ideal e: %.2f", peso);
    }
}