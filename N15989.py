import sys

# N 
# [N - 1, 1] + [N - 1, 2] + [N - 1, 3]
# [N - 2, 3] + [N - 2, 2]
# [N - 3, 3]

MAX_NUM = 10000
N = int(sys.stdin.readline().rstrip())

dp = [[0, 0, 0, 0] for _ in range(MAX_NUM + 1)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1


for i in range(1, MAX_NUM + 1):
    dp[i][1] += (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3])

    if i >= 2:
        dp[i][2] += (dp[i - 2][2] + dp[i - 2][3])

    if i >= 3:
        dp[i][3] += (dp[i - 3][3])

for _ in range(N):
    t = (int(sys.stdin.readline().rstrip()))
    print(sum(dp[t]))
