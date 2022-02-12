#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _venda {
    int cod_peca;
    float preco;
} tp_venda ;

int main() {
    tp_venda A, B;

    A.cod_peca = 1;
    A.preco = 99.99;

    printf("Codigo peca %d \nPreco: %.2f reais \n", A.cod_peca, A.preco);

    B.cod_peca = 2;
    B.preco= 49.50;

    printf("Codigo peca: %d \nPreco: %.2f reais\n", B.cod_peca, B.preco);

    return 0;
}
