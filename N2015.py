import sys, collections, bisect
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = arr[:]
dp_dict = collections.defaultdict(list)

for i in range(1, N):
    dp[i] += dp[i - 1]

for i in range(N):
    dp_dict[dp[i]].append(i)

answer = 0
for i in range(N):
    # CASE 1
    if dp[i] == K:
        answer += 1

    # CASE 2
    key = dp[i] - K
    target = dp_dict[key]
    if target:
        answer += bisect.bisect_left(target, i)
print(answer)



'''
tree = [0 for _ in range(N + 1)]

def update(index, diff):
    while index <= N:
        tree[index] += diff
        index += (index & -index)

def sum(index):
    ret = 0
    while index > 0:
        ret += tree[index]
        index -= (index & -index)
    return ret

for index in range(N):
    update(index + 1, arr[index])

answer = 0
for start in range(1, N + 1):
    for end in range(start, N + 1):
        if sum(end) - sum(start - 1) == K:
            answer += 1
print(answer)
'''