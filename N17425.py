import sys, collections

MAX = 1000001

F = [1 for _ in range(MAX)]
G = [0 for _ in range(MAX)]

T = int(sys.stdin.readline().rstrip())

for i in range(2, MAX):
    for j in range(i, MAX, i):
        F[j] += i

for i in range(1, MAX):
    G[i] = G[i - 1] + F[i]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(G[N])
