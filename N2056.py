import sys

N = int(sys.stdin.readline().rstrip())
DP = [0 for _ in range(N + 1)]

for index in range(1, N + 1):
    arr = sys.stdin.readline().split()
    if len(arr) == 2: # 바로
        DP[index] = int(arr[0])
    else:
        max_time = 0
        for value in map(int, arr[2:]):
            max_time = max(max_time, DP[value])
        DP[index] = int(arr[0]) + max_time
print(max(DP))
