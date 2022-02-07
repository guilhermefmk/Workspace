#include <stdio.h>

#define MAX 10
 
int main() {
 
	int conjunto1[MAX], conjunto2[MAX];
	int mult, temp = 0;
	int tam = 1, tam2 = 1; // tamanho dos dados
	int i = 0, j = 0;
	scanf("%d",&conjunto1[i]);
	
	while((conjunto1[i]>=0)&&(tam<10)){
			i++;
			scanf("%d",&conjunto1[i]);
			tam++;
	}
	scanf("%d",&conjunto2[j]);
	while((conjunto2[j]>=0)&&(tam<10)){
			j++;
			scanf("%d",&conjunto2[j]);
			tam2++;
	}
	for(i=0;i<tam-1;i++){
		mult = conjunto1[i] * conjunto2[i];
		temp = temp + mult;
	}
	printf("Produto escalar: %d", temp);
	printf("\n");

    return 0;
}
