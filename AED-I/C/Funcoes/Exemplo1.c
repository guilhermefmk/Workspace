#include <stdio.h>
#include <stdlib.h>


/* Declaracao - Preciso colocar os ()s mesmo que nao tenha parametros */
void Ola() {
	/* Corpo */
	printf("\n Ola!!! \n");
}


/* ----------------  Programa principal ------------------ */

int main()
{
	printf("\n Programa principal !!");
	
	/* Chamada da funcao */
	Ola();
	
	printf("\n Posso chamar a funcao de novo:");
	
	/* Chamdaa da funcao - Eh necessario chamar com os ()s */
	Ola();
	Ola();
	
	printf("\n Final do Programa!!");
	return 0;
}	
