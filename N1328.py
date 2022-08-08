import sys

MOD = 1000000007
N, L, R = map(int, sys.stdin.readline().split())
DP = [[[-1 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

# TOP-DOWN + Memoization
def dfs(n, l, r):
    if n <= 0:
        return 0

    if DP[n][l][r] != -1:
        return DP[n][l][r]
    
    # 하나 밖에 없는 경우
    if n == 1 and l == 1 and r == 1:
        DP[n][l][r] = 1
        return DP[n][l][r]
    
    # CASE 1 : 내부로
    DP[n][l][r] = dfs(n - 1, l, r) * (n - 2) % MOD

    # CASE 2 : 왼쪽
    if l > 1:
        DP[n][l][r] += dfs(n - 1, l - 1, r)
        DP[n][l][r] %= MOD
    
    # CASE 3 : 오른쪽
    if r > 1:
        DP[n][l][r] += dfs(n - 1, l, r - 1)
        DP[n][l][r] %= MOD
    
    # Memoization
    return DP[n][l][r]

print(dfs(N, L, R))


# BOTTOM-UP + No-Memoization
def dfs_1():
    answer = 0
    stack = list()
    stack.append([N - 1, L - 1, R - 1, 1])

    while stack:
        target, left, right, case_cnt = stack.pop()

        if left + right > target:
            continue

        if target == 0:
            if left == 0 and right == 0:
                answer = (answer + case_cnt) % MOD
        else:
            # CASE 1 왼쪽
            if left > 0:
                stack.append([target - 1, left - 1, right, case_cnt])

            # CASE 2 오른쪽
            if right > 0:
                stack.append([target - 1, left, right - 1, case_cnt])

            # CASE 3 내부로
            hole = N - target - 1 # 들어갈 수 있는 구멍 ex. N = 5 이고 2를 넣을 때, 3 [여기] 4 [여기] 5,  (5 - 2 - 1) = 2 구멍
            if hole > 0 and left + right < target:
                case_cnt = (case_cnt * hole) % MOD
                stack.append([target - 1, left, right, case_cnt])
    return answer

print("accurate", dfs_1())


def dp():
    MOD = 1000000007
    n, l, r = map(int, sys.stdin.readline().split())
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

    dp[1][1][1] = 1

    for i in range(2, n + 1):
        for j in range(1, min(i + 1, l + 1)):
            for k in range(1, min(i + 1, r + 1)):
                dp[i][j][k] = (dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i - 2)) % MOD

    return (dp[n][l][r])