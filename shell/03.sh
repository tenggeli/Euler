#! /bin/bash

var=`expr 2 \* 2`
echo "2*2 = $var"

a=10
b=20
val=`expr $a + $b`
echo "a+b=$val"

val=`expr $a - $b`
echo "a-b=$val"

val=`expr $a \* $b`
echo "a*b=$val"

val=`expr $b / $a`
echo "a/b=$val"

val=`expr $a % $b`
echo "$val"

if [ $a == $b ]
	then 
	echo "succ"
fi

if [ $a != $b ]
	then
	echo "fail"
fi
