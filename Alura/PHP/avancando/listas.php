<?php

$conta1 = [
    'titular' => 'Guilherme',
    'saldo' => 1000
    ];
$conta2 = [
    'titular' => 'Rafael',
    'saldo' => 2000
    ];
$conta3 = [
    'titular' => 'Marcelo', 
    'saldo' => 3000
];
$contasCorrentes = [
                $conta1, 
                $conta2, 
                $conta3
            ];

/*for($i = 0; $i < count($contasCorrentes); $i++){
    echo $contasCorrentes[$i]['titular'] . PHP_EOL;
    echo $contasCorrentes[$i]['saldo'] . PHP_EOL;
}*/

foreach ($contasCorrentes as $conta) {
    echo $conta['titular'] . PHP_EOL;
}

