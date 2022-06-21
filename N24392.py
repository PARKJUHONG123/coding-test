import sys

N, M = map(int, sys.stdin.readline().split())
LEFT = 1000000007
matrix = list()
init_list = [0 for _ in range(M)]

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in reversed(range(N - 1)):
    dp = init_list[:]
    for j in range(M):
        if matrix[i][j] == 1:
            dp[j] = (dp[j] + matrix[i + 1][j]) % LEFT

            if j - 1 >= 0:
                dp[j] = (dp[j] + matrix[i + 1][j - 1]) % LEFT

            if j + 1 < M:
                dp[j] = (dp[j] + matrix[i + 1][j + 1]) % LEFT
    matrix[i] = dp[:]

print(sum(matrix[0]) % LEFT)