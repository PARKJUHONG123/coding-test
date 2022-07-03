import sys, collections

N = int(sys.stdin.readline().rstrip())
parents = [-1 for _ in range(N + 1)]
depths = [-1 for _ in range(N + 1)]

tree = collections.defaultdict(list)
for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].append(B)
    tree[B].append(A)

# DEPTH, PARENT SET DFS
def dfs():
    start_value, start_depth = 1, 1
    stack, visited = list(), list()

    depths[start_value] = start_depth
    parents[start_value] = -1    
    visited.append(start_value)
    stack.append([start_value, start_depth + 1])

    while stack:
        stack_value, stack_depth = stack.pop()
        for child_value in tree[stack_value]:
            if child_value not in visited:
                visited.append(child_value)
                parents[child_value] = stack_value
                depths[child_value] = stack_depth
                stack.append([child_value, stack_depth + 1])

dfs()

def LCA(a, b):
    a_level, b_level = depths[a], depths[b]

    while a_level != b_level:
        if a_level < b_level:
            b = parents[b]
            b_level = depths[b]
        else:
            a = parents[a]
            a_level = depths[a]
    
    while a != b:
        a, b = parents[a], parents[b]
    return a

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a, b))
