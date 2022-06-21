import sys
N = int(sys.stdin.readline().rstrip())
print(sum(k * (N // k) for k in range(1, N + 1)))