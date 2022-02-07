#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct _venda {
    int cod_peca;
    float preco;
} tp_venda;

tp_venda novavenda(int codigo, float preco) {
    tp_venda A;
    A.cod_peca = codigo;
    A.preco = preco;
    return A;
}

void imprimeVenda(tp_venda C) {
    printf("Codigo da peca: %d\nPreco: %.2f reais\n\n", C.cod_peca, C.preco);
}


int main() {
    tp_venda V1, V2;

    V1 = novavenda(5, 100);
    V2 = novavenda(7, 200);

    imprimeVenda(V1);
    imprimeVenda(V2);

    return 0;
}