#!/bin/bash
echo "当前执行脚本的文件名：$0"
echo "第一个参数：$1 "
echo "第二个参数：$2"
echo "传递给脚本或函数的所有参数:$@"
echo "传递给脚本或函数的所有参数:$*"
echo "传递给脚本的参数个数:$#"
echo $?
