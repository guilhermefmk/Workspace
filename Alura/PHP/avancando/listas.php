<?php

$lista = [];

for($i = 0; $i <= 15; $i++){
    $lista[$i] = $i;
}
for($i = 0; $i < count($lista); $i++){
    print("$lista[$i]" . PHP_EOL);
}
