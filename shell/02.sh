#! /bin/bash

a=10
echo -e "value is to $a \n"
#利用反引号可以将执行结果保存在变量中
DATE=`date`
echo -e "this is time $DATE \n"

USERS=`who |wc -l`
echo -e "Login is $USERS \n"

UPDATE=`date;uptime`
echo -e "update is $UPDATE \n"
#变量的替换，根据变量是否为空来进行替换
#${var}	变量本来的值
#${var:-word}	如果变量 var 为空或已被删除(unset)，那么返回 word，但不改变 var 的值。
#${var:=word}	如果变量 var 为空或已被删除(unset)，那么返回 word，并将 var 的值设置为 word。
#${var:?message}	如果变量 var 为空或已被删除(unset)，那么将消息 message 送到标准错误输出，可以用来检测变量 var 是否可以被正常赋值。
#若此替换出现在Shell脚本中，那么脚本将停止运行。
#${var:+word}	如果变量 var 被定义，那么返回 word，但不改变 var 的值。
echo ${var:-"var is not"}
echo -e "1 - var $var \n"

echo ${var:="var is not set"}
echo "2 =  var $var"

unset var
echo ${var:+"this is default value"}
echo -e "3 - var is of $var \n"

var="prift";
echo ${var:+"this is defaut value"}
echo -e "4- var is of $var \n"

echo ${var:?"this is vale"}
echo -e "5- var is $var \n"
