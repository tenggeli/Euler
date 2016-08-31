<?php

$t1 = microtime(true);
$num = 2000000;
$ce_num = ceil(sqrt($num));
$odd = [];
for ($i = 2; $i <= $num ; $i+=1) {
	$odd[$i] = 1;
}

$sum = 0;
for ($i=2 ; $i <= $ce_num + 1 ; $i++) {
	if(isset($odd[$i]) && !empty($odd[$i])){
		for($j = $i * $i; $j <= $num + 1; $j += $i){
			$odd[$j] = 0;
		}
	}
}

foreach ($odd as $key => $value) {
	if($value != 0){
		echo $key,"\n";
		$sum += $key;
	}
}
echo '---',$sum,"\n";
$t2 = microtime(true);
echo (($t2-$t1)*1000).'ms',"\n";
