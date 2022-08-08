import sys

N = int(sys.stdin.readline().rstrip())
matrix = list()


for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def dfs(start_index):
    stack = list()
    stack.append([start_index, 0, [start_index]])
    min_weight = sys.maxsize

    while stack:
        print(stack)
        cur_index, cur_weight, visited = stack.pop()

        if len(visited) == N:
            final_index = visited[-1]
            final_weight = matrix[final_index][start_index]
            if final_weight != 0:
                min_weight = min(min_weight, cur_weight + final_weight)
        else:
            for next_index in range(N):
                if next_index not in visited:
                    next_weight = matrix[cur_index][next_index]
                    if next_weight == 0:
                        continue
                    stack.append([ next_index, cur_weight + next_weight, visited + [next_index] ])
    return min_weight

answer = dfs(0)
print(answer)