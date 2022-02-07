#include <stdio.h>
#include <stdlib.h>
int soma1010() {
    int A;
    A = 10+10;

    return A;
}




int main ()
{
    int N, Resultado;

    printf("\n Entre com N: ");
    scanf("%d",&N);

    Resultado = N * soma1010() + 20 * soma1010() * (20+20);

    printf("\n\n O resultado é %d ", Resultado);
    
    return 0;
}