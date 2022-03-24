<?php

class conta
{
     public string $cpfTitular;
     public string $nomeTitular;
     public float $saldo = 0;


     public function sacar(float $valorASacar) : void
     {
          if ($valorASacar > $this->saldo) {
               echo "Saldo insuficiente" . PHP_EOL;
          }else{
               $this->saldo -= $valorASacar;
               echo "Saque efetuado, valor atual : $this->saldo" . PHP_EOL;
          }
     }

     public function  depositar(float $valorADepositar) : void
     {
          if ($valorADepositar > 0) {
               $this->saldo += $valorADepositar;
          } else {
               echo "Valor menor ou igual a zero" . PHP_EOL;
          }
     }

}