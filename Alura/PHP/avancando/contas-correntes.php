<?php
    
    
    $contascorrentes = [
        '123.456.789-10' => [
            'titular' => 'Guilherme',
            'saldo' => 1234
        ],
        '234.567.891-01' => [
            'titular' => 'Rafael',
            'saldo' => 2738
        ],
        '334.567.891-01' => [
            'titular' => 'Marcelo',
            'saldo' => 8477
        ]
    ];
    
    $contascorrentes['123.456.789-10']['saldo'] = sacar(pegasaldo('123.456.789-10', $contascorrentes), 1500);
    $contascorrentes['334.567.891-01']['saldo'] = depositar(pegasaldo('334.567.891-01', $contascorrentes), -45);


    foreach ($contascorrentes as $cpf => $conta) {
        exibemensagem($cpf . " " . $conta['titular'] . " " . $conta['saldo']);
    }
    


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
        echo $mensagem . PHP_EOL;
    }
?>