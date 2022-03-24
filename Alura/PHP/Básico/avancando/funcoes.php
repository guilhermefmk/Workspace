<?php
function sacar(int $saldo,float $saque){
        if ($saldo - $saque < 0) {
            exibemensagem('Saldo insuficiente');
        } else {
            $saldo -= $saque;
        }
        return $saldo;
    }
function depositar(int $saldo,float $deposito){

    if ($deposito > 0) {
        $saldo += $deposito;
    } else {
        exibeMensagem("Depositos precisam ser positivos");
    }
    return $saldo;
}
function pegasaldo($cpf, $array){
    $saldo = $array[$cpf]['saldo'];
    return $saldo;
}
function exibemensagem($mensagem) {
    echo $mensagem . '<br>';
}

function exibeconta(array $conta){
    echo '<li>Titular: $conta[titular]. Saldo: $conta[saldo]</li>';
}
?>