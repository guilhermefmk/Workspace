#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 10

typedef struct _conta {
    int cod;
    char nome[30];
    float saldo;
} conta;


int main()
{
    conta contas[TAM];
    int i;
    float saque, saldo;


    for(i=0;i<TAM;i++){
        scanf("%d",&contas[i].cod);
        scanf("%s",contas[i].nome);
        scanf("%f",&contas[i].saldo);
    }
    scanf("%f",&saque);
    for(i=0;i<TAM;i++) {
        saldo = contas[i].saldo - saque;
        printf("%d\n",contas[i].cod);
        printf("%s\n",contas[i].nome);
        if (saldo>0)
            printf("%.2f\n",saldo);
        else
            printf("Saldo insuficiente.\n");
    }
    return 0;
}