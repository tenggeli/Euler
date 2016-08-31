<?php

$a =0 ;
for($i = 1; $i <=20000000 ; $i++ ){
	$x = isPrime($i);
	if($x != false){
        echo $a,'===',"\n";
		$a += $x;
		if($i ==20000000 ){
			echo 'data',$a,"\n";die;
		}
	}
}


//求质数
function isPrime($n) {//TurkHackTeam AVP production
        for ($i = 5; $i * $i <= $n; $i += 6) {
            if ($n % $i === 0 || $n % ($i + 2) === 0) {
                return false;
            }
        }
        return $n;
}
