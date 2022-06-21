import sys, math

N, M = map(int, sys.stdin.readline().split())
height = math.ceil(math.log(N, 2)) + 1
tree_size = pow(2, int(height) + 1)

arr = list()
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

MAX = max(arr)
tree = [0 for _ in range(tree_size)]

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2

    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]

init(0, N - 1, 1)

def interval_min(start, end, index, left, right):
    if left > end or right < start:
        return MAX
    
    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return min(interval_min(start, mid, index * 2, left, right), interval_min(mid + 1, end, index * 2 + 1, left, right))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(interval_min(0, N - 1, 1, a - 1, b - 1))