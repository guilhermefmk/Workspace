<?php
    
    include 'funcoes.php';
    
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

    echo "<ul>";
    foreach ($contascorrentes as $cpf => $conta) {
        exibeconta($conta);
    }
    echo "</ul>";


    
?>