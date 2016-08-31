#! /bin/sh

a=10
b=20
#-eq 相当于==
if [ $a -eq $b ] 
	then
		echo "ab 相等"
	else
		echo "ab 不相等" 
fi

#-ne 相当于 !=
if [ $a -ne $b ]
	then 
		echo "ab 不相等"
	else
		echo "ab 相等"
fi

#-gt 相当于>
if [ $a -gt $b ]
	then 
		echo "a 大于 b"
	else
		echo "a 小于 b"
fi

#-lt 相当于 <
if [ $a -lt $b ]
	then 
		echo "a 小于 b"
	else
		echo "a 大于 b"
fi

#-ge 相当于 >=
if [ $a -ge $b ]
	then 
		echo "a大于等于 b"
	else
		echo "a不大于等于b"
fi

#-le 相当于<=
if [ $a -le $b ]
	then 
		echo "a小于等于b"
	else
		echo "a不小于等于b"
fi
