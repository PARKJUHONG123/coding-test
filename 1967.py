import sys, collections

tree = collections.defaultdict(list)

N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(0)
    exit()

for _ in range(N - 1):
    start, end, weight = map(int, sys.stdin.readline().split())
    tree[start].append([end, weight])
    tree[end].append([start, weight])

def dfs(start):
    stack = list()
    stack.append([start, 0])
    max_index, max_weight = -1, -1
    visited = [False for _ in range(N + 1)]
    visited[start] = True

    while stack:
        cur, cur_weight = stack.pop()
        if max_weight < cur_weight:
            max_weight = cur_weight
            max_index = cur

        for next, next_weight in tree[cur]:
            if not visited[next]:
                visited[next] = True
                stack.append([next, cur_weight + next_weight])
    return max_index, max_weight

start_index, start_weight = dfs(1)
end_index, end_weight = dfs(start_index)

print(end_weight)