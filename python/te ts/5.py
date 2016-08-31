#coding:utf-8
#求具有五百个因子的三角形数
#如何判断一个数是否三角形数？
#第n个三角形数是前n个数的和
#求出所有因子.求出数的因子存放数组中。如果数组大于500。，done

#求第n个三角形数
def sum_a(i):
    sum = 0
    for x in range(0,i+1):
        sum += x
    return sum 


def trian_num(i):
    x = []
    if(i%2 == 0 ):
        i = i/2
    else:
        i = (i+1)/2
    num = 0
    for y in range(1,i):
        if i%y == 0:
            num +=1
        
    return num
    
for num in range(1000,10000):
    x = sum_a(num)
    y = trian_num(x)
    print y
    print "\n"
    lenx = y
    if(lenx == 500):
        print x
 
     
