#coding:utf-8
import math
def pro_num(num):
    p = [True] * (num + 1)
    p[0] = p[1] = False
    pro = []
    
    for i in range(2, int(num ** .5 + 1.5)):
        if not p[i]:
            continue
        for j in range(i * i, num + 1, i):
            p[j] = False
            pro.append(j)
    return pro
print pro_num(10)
