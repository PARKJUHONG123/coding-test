import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

A, B = list(), list()

for value in arr:
    if not A:
        A.append(value)
        B.append(value)
        continue

    if value > 0: # 0 보다 크면 추가
        B.append(max(B[-1] + value, value)) # 하나 빼먹을 리스트
        A.append(max(A[-1] + value, value)) # 계속 추가할 리스트

    else: # 0 보다 작으면
        B.append(max(max(B[-1] + value, A[-1]), value)) # 현재 값을 빼먹고 넘길건지 (A[-1]), 이전에 값을 빼먹었을 가능성이 있는 것에서 현재 값을 추가 (B[-1] + value)
        A.append(max(A[-1] + value, value)) # 현재 값 계속 추가 # 계속 추가할 리스트

print(max(max(A), max(B)))
