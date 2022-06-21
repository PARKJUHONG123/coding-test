import sys
MAX = 1000001

M, N = map(int, sys.stdin.readline().split())

dp = [False for _ in range(MAX)]
dp[1] = True

for i in range(2, MAX):
    for j in range(i * 2, MAX, i):
        dp[j] = True

for i in range(M, N + 1):
    if not dp[i]:
        print(i)