import sys, collections

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def bfs(trash_x, trash_y, trash_matrix, trash_cnt):
    visited = [[False for _ in range(w)] for _ in range(h)]

    queue = collections.deque()
    queue.append([trash_x, trash_y, 1])
    trash_matrix[trash_x][trash_y] = '.'
    trash_cnt -= 1
    visited[trash_x][trash_y] = True
    total_cnt = 0

    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    value = trash_matrix[dx][dy]
                    if value == '*':
                        trash_cnt -= 1
                        trash_matrix[dx][dy] = '.'
                        total_cnt += cnt

                        if trash_cnt == 0:
                            return (dx, dy, total_cnt)
                        else:
                            visited = [[False for _ in range(w)] for _ in range(h)]
                            queue = collections.deque()
                            queue.append([dx, dy, 1])

                    elif value == '.':
                        queue.append([ dx, dy, cnt + 1 ])
    return (-1, -1, -1)


def bfs_start(start_x, start_y, end_x, end_y, trash_matrix):
    queue = collections.deque()
    queue.append([start_x, start_y, 1])
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[start_x][start_y] = True

    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    value = trash_matrix[dx][dy]
                    if value != 'x':
                        if dx == end_x and dy == end_y:
                            return cnt
                        else:
                            queue.append([dx, dy, cnt + 1])
    return -1

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = [['.' for _ in range(w)] for _ in range(h)]
    trash = list()
    for i in range(h):
        tmp = sys.stdin.readline()
        for j in range(w):
            if tmp[j] == 'o':
                o_point = [i, j]
                matrix[i][j] = '.'
            elif tmp[j] == '*':
                matrix[i][j] = tmp[j]
                trash.append([i, j])
            else:
                matrix[i][j] = tmp[j]
    trash_cnt = len(trash)

    if trash_cnt != 0:
        flag = False
        min_length = sys.maxsize
        for value in trash:
            start_x, start_y, start_cnt = bfs(value[0], value[1], [row[:] for row in matrix], trash_cnt)
            to_start = bfs_start(o_point[0], o_point[1], start_x, start_y, [row[:] for row in matrix])            
            if start_cnt == -1:
                print(-1)
                flag = True
                break
            else:
                min_length = min(min_length, start_cnt + to_start)
        if not flag:
            print(min_length)