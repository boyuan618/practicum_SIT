<?php
$m = 5; 
$n = 10; 
$sum_of_factorials = calculate_sum_of_factorials($m, $n); 
echo "m! + n! = " . $sum_of_factorials; 
function calculate_sum_of_factorials($argument1, $argument2) 
{ 
$factorial1 = calculate_factorial($argument1); 
$factorial2 = calculate_factorial($argument2); 
$result = calculate_sum($factorial1, $factorial2); 
return $result;   
} 
function calculate_factorial($argument) 
{ 
$factorial_result = 1; 
for ($i = 1; $i <= $argument; $i++)
{ 
$factorial_result = $factorial_result * $i; 
} 
return $factorial_result; 
} 
function calculate_sum($argument1, $argument2) 
{ 
return $argument1 + $argument2; 
} 
?>