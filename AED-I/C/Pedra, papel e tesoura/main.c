#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include<time.h>



int main(){
    
    //VARIÁVEIS
    bool jogando = true, numValido = false;
    char arr[3][20] = {"Pedra", "Papel", "Tesoura"}, *opcaoCharJogador, *opcaoCharMaquina;
    int opJogador, opMaquina;


    while (jogando){


        printf("Digite o número conforme as opções:\n (1)Pedra -- (2)Papel -- (3)Tesoura\n");
        while (!numValido){
            scanf("%d", &opJogador);
            if(opJogador == 1 || opJogador == 2 || opJogador == 3)
                numValido = true;
            else
                printf("Número inválido!\nDigite o número conforme as opções:\n (1)Pedra -- (2)Papel -- (3)Tesoura\n");
        }
        
        srand(time(NULL));
        opMaquina = rand() % 3;

        opcaoCharJogador = arr[opJogador-1];
        opcaoCharMaquina = arr[opMaquina];
        



        return 0;
    }
}