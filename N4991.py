import sys
from collections import deque

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def all_cleaned():
    for i in range(h):
        if '*' in matrix[i]:
            return False
    return True

def bfs():
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append([start, 1])
    last_count = 0
    while queue:
        [x, y], count = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy]:
                    value = matrix[dx][dy]
                    if value == '.':
                        visited[dx][dy] = True
                        queue.append([[dx, dy], count + 1])
                    elif value == '*':
                        print(dx, dy, count, matrix[dx][dy])
                        matrix[dx][dy] = '.'
                        last_count += count
                        if all_cleaned():
                            print(last_count)
                            return
                        queue = deque()
                        visited = [[False for _ in range(w)] for _ in range(h)]
                        queue.append([[dx, dy], 1])
                        visited[dx][dy] = True
                        break
    print(-1)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = [['.' for _ in range(w)] for _ in range(h)]
    start = []
    for i in range(h):
        tmp = sys.stdin.readline()
        for j in range(w):
            if tmp[j] == 'o':
                start = [i, j]
                matrix[i][j] = '.'
            else:
                matrix[i][j] = tmp[j]
    bfs()



