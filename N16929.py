import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]

matrix = list()
for _ in range(N):
    element = input().rstrip()
    matrix.append(element)
visited = [[-1 for _ in range(M)] for _ in range(N)]

def get_non_visited():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == -1:
                return i, j
    return -1, -1

def dfs(i, j):
    stack = list()
    target = matrix[i][j]
    stack.append([i, j, 0])

    while stack:
        si, sj, sv = stack.pop()
        visited[si][sj] = sv

        for di, dj in D:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if matrix[ni][nj] == target:
                    if visited[ni][nj] == -1:
                        stack.append([ni, nj, sv + 1])
                    else:
                        if abs(visited[ni][nj] - sv) >= 3:
                            return True
    return False


def get_answer():
    while True:
        gi, gy = get_non_visited()
        if gi == -1 and gy == -1:
            return "No"
        else:
            ret = dfs(gi, gy)
            if ret:
                return "Yes"

print(get_answer())