import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
N, M = len(A), len(B)
DP = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
answer = []

for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            DP[i + 1][j + 1] = DP[i][j] + 1
        else:
            DP[i + 1][j + 1] = max(DP[i][j + 1], DP[i + 1][j])

n, m = N, M
while DP[n][m] != 0:
    if DP[n][m] == DP[n - 1][m] or DP[n][m] == DP[n][m - 1]:
        if DP[n - 1][m] == DP[n][m - 1]:
            n = n - 1
        elif DP[n][m] == DP[n - 1][m]:
            n = n - 1
        else:
            m = m - 1
    else:
        answer.append(B[m - 1])
        n, m = n - 1, m - 1

print(DP[N][M])
print(''.join(answer[::-1]))