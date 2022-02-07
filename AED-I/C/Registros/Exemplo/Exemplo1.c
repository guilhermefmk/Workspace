#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    typedef struct pessoa {
        char nome[20];
        int idade;
        int RG;
    }tp_pessoa;

    tp_pessoa p1,p2;


    strcpy(p1.nome, "Joao");
    p1.idade = 50;
    p1.RG = 567891011;
    printf(" Nome: %s\n Idade: %d\n RG: %d\n",
                    p1.nome, p1.idade, p1.RG);

    strcpy(p2.nome, "Maria");
    p2.idade = 15;
    /*p2.RG = 32133122;*/
    printf(" Nome: %s\n Idade: %d\n RG: %d\n",
                    p2.nome,p2.idade, p2.RG);
    return 0;
}