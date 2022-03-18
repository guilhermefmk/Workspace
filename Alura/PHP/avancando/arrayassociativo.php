<?php
$string = "angelo";
$arrayassociativo = [
    'teste' => $string,
    'teste2' => 'grupo',
    'teste3' => 'gui'
];


foreach ($arrayassociativo as $item) {
    echo $item . PHP_EOL;
}

?>