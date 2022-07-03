import sys

N, M = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + arr[i][j]

for i in range(N):
    print(dp[i])

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - ( dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1] ) )


'''
tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

def update(x, y, diff):
    tx = x
    while tx <= N:
        ty = y
        while ty <= N:
            tree[tx][ty] += diff
            ty += (ty & -ty)
        tx += (tx & -tx)

def sum_branch(x, y):
    ret, tx = 0, x
    while tx > 0:
        ty = y
        while ty > 0:
            ret += tree[tx][ty]
            ty -= (ty & -ty)
        tx -= (tx & -tx)
    return ret

for i in range(1, N + 1):
    element = [0] + list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        update(i, j, element[j])

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ret = (sum_branch(x2, y2) - sum_branch(x1 - 1, y2)) - (sum_branch(x2, y1 - 1) - sum_branch(x1 - 1, y1 - 1))
    print(ret)
'''