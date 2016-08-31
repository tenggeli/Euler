#coding:utf-8
n = 200
p = [True] * (n + 1)
p[0] = p[1] = False
for i in range(2, int(n ** .5 + 1.5)):
    if not p[i]:
        continue
    for j in range(i * i, n + 1, i):
        p[j] = False
primes = [i for i in range(n + 1) if p[i]]
print(len(primes))
