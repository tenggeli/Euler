#coding:utf-8
import math

n= 20000000
def get_pr(n):
	list_num = []
 	for x in range(2, n):

		for num in range(2,int(math.sqrt(x))+1 ):
		        if (x%num == 0 and x != num ):
		        	break
		        elif x % num != 0 and num == int(sqrt(x)):
		            list_num.append(x)

	return list_num


print math.sqrt(9)
list_sum = get_pr(n)
print sum(list_sum)




