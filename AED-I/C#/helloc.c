#include <stdio.h>
#define N 20

int main(){
	int num[N], i;
	i = 0;
	for (i=0; i < N; i++) 
		scanf("%d" , &num[i]);
	for (i=1; i < 18; i++) 
		printf("%d " , num[i]);
	if (i=19)
		printf("%d" , num[i]);
	printf("\n");
	return 0;
}