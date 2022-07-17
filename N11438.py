import sys, collections, math

N = int(sys.stdin.readline().rstrip())
D = int((math.log2(N)) // 1) + 1

depths = [-1 for _ in range(N + 1)]
parents = [[0 for _ in range(D)] for _ in range(N + 1)]

tree = collections.defaultdict(list)

for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].append(B)
    tree[B].append(A)

# DEPTH, PARENT SET DFS
def dfs():
    start_value, start_depth = 1, 1
    stack = list()
    visited = [False for _ in range(N + 1)]

    depths[start_value] = start_depth
    visited[start_value] = True
    stack.append([start_value, start_depth + 1])

    while stack:
        stack_value, stack_depth = stack.pop()

        for child_value in tree[stack_value]:
            if not visited[child_value]:
                visited[child_value] = True
                
                depths[child_value] = stack_depth
                parents[child_value][0] = stack_value
                stack.append([child_value, stack_depth + 1]) 

def set_parent():
    dfs()
    for i in range(1, D):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]

set_parent()

def LCA(a, b):
    if depths[a] > depths[b]:
        a, b = b, a
    
    for i in range(D - 1, -1, -1):
        if depths[b] - depths[a] >= 2 ** i:
            b = parents[b][i]
    
    if a == b:
        return a

    for i in range(D - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a, b = parents[a][i], parents[b][i]

    return parents[a][0]

M = int(sys.stdin.readline().rstrip())


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a, b))
