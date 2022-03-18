#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include<time.h>



int main(){
    
    //VARIÁVEIS
    bool jogando = true;
    char arr[3][20] = {"Pedra", "Papel", "Tesoura"}, *opcaoCharMaquina;
    int opJogador, opMaquina, jogarnov;


    while (jogando){
		bool numValido = false;

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

        opcaoCharMaquina = arr[opMaquina];
        
        printf("O seu adversario escolheu %s\n", opcaoCharMaquina);
	
        if((opJogador == 1 && opMaquina == 2) || (opJogador == 3 && opMaquina == 1) || (opJogador == 2 && opMaquina== 0)){
            printf("Ganhou!\n");
        }
        if((opJogador == 1 && opMaquina == 1) || (opJogador == 3 && opMaquina == 0) || (opJogador == 2 && opMaquina == 2)){
            printf("Perdeu!\n");
        }
        if(opJogador == opMaquina+1){
            printf("Empate!\n");
    
        }
        printf("Jogar novamente?");
        scanf("%d", &jogarnov);
        if(jogarnov == 1){
            jogando = false;
        }
        
    }
    return 0;
}
