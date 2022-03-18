<?php


for($i = 1; $i < 100; $i++){
    if($i % 2 == 1){
        print("$i" . PHP_EOL);
    }
    else{
        continue;
    }
}