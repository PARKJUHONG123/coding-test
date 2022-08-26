import sys, collections

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
INF = sys.maxsize
P = collections.defaultdict(collections.defaultdict)

for _ in range(M):
    S, D, C = map(int, sys.stdin.readline().split())
    if S in P:
        if D in P[S]:
            P[S][D] = min(C, P[S][D])
        else:
            P[S][D] = C
    else:
        P[S][D] = C

D = [INF for _ in range(N + 1)]
start, end = map(int, sys.stdin.readline().split())

def bfs(start):
    D[start] = 0
    queue = collections.deque()
    queue.append(start)
    visited = [True] + [False for _ in range(N)]

    while queue:
        cur = queue.popleft()
        visited[cur] = True
        if cur == end: 
            return D[end]

        for next in P[cur].keys():
            if not visited[next]:
                left = D[cur] + P[cur][next]
                right = D[next]
                if left < right:
                    D[next] = left
        
        min_index, min_distance = -1, INF
        for index in range(1, N + 1):
            if not visited[index]:
                if D[index] < min_distance:
                    min_index, min_distance = index, D[index]
        queue.append(min_index)
    return D[end]

print(bfs(start))