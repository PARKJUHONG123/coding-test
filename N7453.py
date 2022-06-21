import sys

N = int(sys.stdin.readline().rstrip())

AB = dict()
A, B, C, D = list(), list(), list(), list()

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        sum_ab = a + b
        if sum_ab in AB:
            AB[sum_ab] += 1
        else:
            AB[sum_ab] = 1
    
ret = 0

for c in C:
    for d in D:
        sum_cd = -(c + d)
        if sum_cd in AB:
            ret += AB[sum_cd]

print(ret)