#include <stdio.h>
#include <stdlib.h>

int soma(int x, int y) 
{
    int result;
    result = x + y;

    return result;
}



int main()
{
    int N, resultado;
	
	printf("Entre com o numero N : ");
    scanf("%d", &N);

    resultado = N * soma(10,10) + 20 * soma(10,10) + 30 * soma(20,20);

    printf("\n\n  O resultado e %d ", resultado);

}
