import sys, collections, math

N = int(sys.stdin.readline().rstrip())
P = int(math.log2(N) // 1) + 1

tree = collections.defaultdict(collections.defaultdict)

for _ in range(N - 1):
    S, E, D = map(int, sys.stdin.readline().split())
    tree[S][E] = D
    tree[E][S] = D

DEPTH = [-1 for _ in range(N + 1)]
PARENT = [[0 for _ in range(P)] for _ in range(N + 1)]
DISTANCE = [0 for _ in range(N + 1)]

def set_depth():
    stack = list()
    stack.append((1, 0, 0))
    DEPTH[1] = 0
    DISTANCE[1] = 0

    while stack:
        root, depth, distance = stack.pop()
        for leaf in tree[root]:
            if DEPTH[leaf] == -1:
                PARENT[leaf][0] = root
                DEPTH[leaf] = depth + 1
                DISTANCE[leaf] = distance + tree[root][leaf]
                stack.append((leaf, depth + 1, distance + tree[root][leaf]))

def set_parent():
    set_depth()
    for i in range(1, P):
        for j in range(1, N + 1):
            PARENT[j][i] = PARENT[PARENT[j][i - 1]][i - 1]

def get_common_parent(A, B):
    target, standard = A, B
    if DEPTH[target] < DEPTH[standard]:
        target, standard = standard, target
    
    for i in range(P - 1, -1, -1):
        if DEPTH[target] - DEPTH[standard] >= 2 ** i:
            target = PARENT[target][i]

    if target == standard:
        return target

    for i in range(P - 1, -1, -1):
        if PARENT[standard][i] != PARENT[target][i]:
            standard, target = PARENT[standard][i], PARENT[target][i]

    return PARENT[target][0]

def get_distance(A, B):
    parent = get_common_parent(A, B)
    return DISTANCE[A] + DISTANCE[B] - 2 * DISTANCE[parent]

M = int(sys.stdin.readline().rstrip())
set_parent()

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(get_distance(S, E))





def solution_DP(): # 메모리 초과
    N = int(sys.stdin.readline().rstrip())

    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(N - 1):
        S, E, D = map(int, sys.stdin.readline().split())
        DP[S][E] = D
        DP[E][S] = D

    visited = [False for _ in range(N + 1)]

    def dfs(start, end):
        if DP[start][end] != 0:
            return DP[start][end]
        
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = True
                if DP[start][i] != 0:
                    if DP[end][i] != 0:
                        DP[start][end] = DP[end][start] = DP[start][i] + DP[i][end]
                        break
                    else:
                        DP[start][end] = DP[end][start] = dfs(i, end) + DP[start][i]
                        break
                else:
                    if DP[end][i] != 0:
                        DP[start][end] = DP[end][start] = dfs(start, i) + DP[i][end]
                        break
                visited[i] = False

        return DP[start][end]


    M = int(sys.stdin.readline().rstrip())
    for _ in range(M):
        TS, TE = map(int, sys.stdin.readline().split())
        visited[TS] = visited[TE] = True
        print(dfs(TS, TE))
        visited[TS] = visited[TE] = False
