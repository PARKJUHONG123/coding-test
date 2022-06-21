import sys, collections
N, Q = map(int, sys.stdin.readline().split())

map_dict = collections.defaultdict(list)

for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().split())
    map_dict[p].append((q, r))
    map_dict[q].append((p, r))

def dfs(K, V):
    stack = list()
    stack.append(V)
    visited = set()

    while stack:
        sv = stack.pop()
        visited.add(sv)

        for mv, kv in map_dict[sv]:
            if mv not in visited:
                visited.add(sv)
                if kv >= K:                    
                    stack.append(mv)
    return len(visited) - 1

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(dfs(k, v))