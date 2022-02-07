#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 10

typedef struct _pessoa {
    char nome[30];
    char sobrenome[30];
    int idade;
} tp_pessoa;

int main() {
    tp_pessoa pessoas[TAM];
    int i;
    char *ret1, *ret2, busca[100];

    for(i=0;i<TAM;i++){
        scanf("%s",pessoas[i].nome);
        scanf("%s",pessoas[i].sobrenome);
        scanf("%d",&pessoas[i].idade);
    }
    
    scanf("%s",busca);

    for(i=0;i<TAM;i++) {
        ret1 = strcasestr(pessoas[i].nome, busca);
        ret2 = strcasestr(pessoas[i].sobrenome, busca);
        if (ret1){
            printf("%s\n", pessoas[i].nome);
            printf("%s\n", pessoas[i].sobrenome);
            printf("%d\n", pessoas[i].idade);
        }
        else if (ret2){
            printf("%s\n", pessoas[i].nome);
            printf("%s\n", pessoas[i].sobrenome);
            printf("%d\n", pessoas[i].idade);
        }
	}
    return 0;
}
