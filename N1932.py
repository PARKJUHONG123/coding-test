import sys

n = int(sys.stdin.readline().rstrip())

ret = [0 for _ in range(n)]

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    dp = ret[:]
    for j in range(i + 1):
        if j == 0:
            dp[j] = ret[j] + a[j]
    
        else:
            dp[j] = max(ret[j - 1] + a[j], ret[j] + a[j])
    ret = dp[:]

print(max(ret))