#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>

int main(){
    int n = 1, i; 
    float valores[20], media, soma = 0;

    while(n>0){
        scanf("%d", &n);
        
        for(i=0;i <n;i++){
            float aux;
            scanf(" %f", &aux);
            valores[ i ] = aux;
            soma += valores[ i ];
        }
        media = soma/n;
        printf("%f", media);
    }
    return 0;
}