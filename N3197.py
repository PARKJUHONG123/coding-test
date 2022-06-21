import sys, collections

R, C = map(int, sys.stdin.readline().split())

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
matrix = list()

bird = collections.deque()
melt = collections.deque()

bird_visited = [[False for _ in range(C)] for _ in range(R)]
melt_visited = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
    t = list(sys.stdin.readline().rstrip())
    matrix.append(t)
    for j in range(C):
        if t[j] == 'L':
            if bird:
                target = [i, j]
            else:
                bird.append([i, j])
            melt.append([i, j])
        elif t[j] == '.':
            melt.append([i, j])

def bfs(bird, melt):
    ret = 0
    while melt and bird:
        next_bird = collections.deque()
        next_melt = collections.deque()

        while bird:
            bx, by = bird.popleft()
            if bx == target[0] and by == target[1]:
                return ret
            bird_visited[bx][by] = True

            for dx, dy in d:
                nx, ny = bx + dx, by + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if not bird_visited[nx][ny]:
                        bird_visited[nx][ny] = True
                        if matrix[nx][ny] != 'X' or melt_visited[nx][ny]:
                            bird.append([nx, ny])
                        else:
                            next_bird.append([nx, ny])
        while melt:
            mx, my = melt.popleft()
            melt_visited[mx][my] = True

            for dx, dy in d:
                nx, ny = mx + dx, my + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if not melt_visited[nx][ny]:
                        melt_visited[nx][ny] = True
                        if matrix[nx][ny] != 'X':
                            melt.append([nx, ny])
                        else:
                            next_melt.append([nx, ny])
        bird = next_bird
        melt = next_melt
        ret += 1

print(bfs(bird, melt))