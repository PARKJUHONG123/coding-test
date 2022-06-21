import sys, collections

N, L = map(int, sys.stdin.readline().split())
D = list()

for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        if i == 0 and j == 0:
            continue
        D.append([i, j])

dp = [ [ [ [ [ 0 for _ in range(L + 1) ] for _ in range(N) ] for _ in range(N) ] for _ in range(N) ] for _ in range(N) ]

matrix = list()
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        dp[i][j][i][j][0] += 1

        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if matrix[i][j] == matrix[ni][nj]:            
                    dp[i][j][ni][nj][1] += 1

for length in range(2, L):
    for i in range(N):
        for j in range(N):
            
            for ti in range(N):
                for tj in range(N):

                    if matrix[i][j] != matrix[ti][tj]:
                        continue

                    for di, dj in D: # departure
                        si, sj = i + di, j + dj
                        if 0 <= si < N and 0 <= sj < N:

                            for ai, aj in D: # arrival
                                ei, ej = ti + ai, tj + aj
                                if 0 <= ei < N and 0 <= ej < N:

                                    if matrix[si][sj] == matrix[ei][ej]:
                                        dp[si][sj][ei][ej][length] += dp[i][j][ti][tj][length - 2]

ret = 0
for i in range(N):
    for j in range(N):
        for ti in range(N):
            for tj in range(N):
                ret += dp[i][j][ti][tj][L - 1]

print(ret)