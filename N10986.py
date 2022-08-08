import sys, collections

N, M = map(int, sys.stdin.readline().split())
DP = list(map(int, sys.stdin.readline().split()))

DP[0] %= M
for i in range(1, N):
    DP[i] += DP[i - 1]
    DP[i] %= M

num_dict = collections.defaultdict(int)

for i in range(N):
    num_dict[DP[i]] += 1

answer = num_dict[0]
for num in num_dict:
    N = num_dict[num] - 1
    answer += ((N + 1) * N) // 2

print(answer)