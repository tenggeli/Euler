<?php

for ($i=1; $i <= 1000 ; $i++) {
	for ($j=1; $j <= 1000 ; $j++) {
		for ($a=1; $a <= 1000 ; $a++) {
			if($i + $j + $a == 1000){
				if(pow($i,2) + pow($j,2) == pow($a,2) ){
					echo $i * $j * $a;
					die;
				}
			}
		}
	}
}
