#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>

int main(){

    int n = 1, i, cont = 0; 
    float valores[500], media, soma = 0, somadif=0, resultados[500];
    
          
    while(n>0){
        scanf("%d", &n);
        if(n > 0){


            float somadif=0, soma = 0;


            for(i = 0;i <n; i++){
                float aux;
                scanf(" %f", &aux);
                valores[ i ] = aux;
                soma += valores[ i ];
            }


            media = soma/n;


            for(i = 0;i < n; i++){
                if(valores[i]>media){
                    somadif = somadif + (valores[i] - media);
                }
            }
            resultados[cont] = somadif;
            cont ++;

        }
    }

    for(i = 0; i < cont; i++){
        printf("%.2f\n", resultados[i]);
    }
    return 0;
}