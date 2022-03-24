<?php

require 'conta.php';
$primeiraConta = new Conta();
$primeiraConta -> cpfTitular = '012.345.789-10';
$primeiraConta -> nomeTitular = 'Guilherme';
$primeiraConta -> saldo = 5488;
$segundaConta = new Conta();
$segundaConta -> cpfTitular = '213.312.789-10';
$segundaConta -> nomeTitular = 'Patricia';
$segundaConta -> saldo = 1200;
$primeiraConta->sacar(2000);
$primeiraConta->depositar(0);
var_dump($primeiraConta);
var_dump($segundaConta);